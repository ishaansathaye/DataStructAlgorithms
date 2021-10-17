class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        '''pointer to next element'''
        self.next = next

class LinkedList:
    def __init__(self):
        '''points to the head of the linked list'''
        self.head = None 

    def insert_at_beginning(self, data):
        '''inserting data value at the beginning of linked list'''
        '''first argument is the data value and the next is the one being inserted'''
        node = Node(data, self.head)
        '''make the head element the one that was inserted'''
        self.head = node
    
    def insert_at_end(self, data):
        '''check if linked list is empty'''
        if self.head is None:
            '''head is the node created using the data'''
            '''second argument is next (after last is None)'''
            self.head = Node(data, None)
            return
        
        '''linked list is not blank:'''
        '''go to the end and insert there'''
        iterator = self.head
        while iterator.next:
            '''if iterator.next has some value that means it is not the end'''
            '''keep iterating'''
            iterator = iterator.next
        '''when iterator.next becomes none then insert new node'''
        iterator.next = Node(data, None)
    
    def insert_values(self, data_list):
        '''wiping all current values and inserting new ones'''
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        '''getting length of linked list'''
        count = 0
        iteration = self.head
        '''saying while iteration is not None'''
        while iteration:
            count += 1
            iteration = iteration.next
        return count

    def remove_at(self, index):
        '''check if given index is in bounds'''
        if index < 0 or index >= self.get_length():
            '''throwing an exception'''
            raise Exception("Invalid index")
        
        '''if index is the head or the first'''
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iteration = self.head
        '''iterating through the linked list'''
        while iteration:
            '''want to stop at the element before given index to remove link to that element'''
            if count == (index-1):
                '''make previous element link point to the element after the one that is being removed'''
                iteration.next = iteration.next.next
                break
            iteration = iteration.next
            count += 1
    
    def insert_at(self, index, data):
        '''check if given index is in bounds'''
        if index < 0 or index >= self.get_length():
            '''throwing an exception'''
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        iteration = self.head
        while iteration:
            '''want to stop at the element before given index to modify link to that element'''
            if count == (index-1):
                '''create node for data and next would be the element you are inserting at, since right now at previous element'''
                node = Node(data, iteration.next)
                '''setting previous element's link to point to new element'''
                iteration.next = node
                break
            iteration = iteration.next
            count += 1

    def print(self):
        '''first element is blank in linked list'''
        if self.head is None:
            print("Linked list is empty")
            return

        '''temp var'''
        iterator = self.head
        llstr = ''
        while iterator:
            '''printing data in linked list and showing link between them'''
            llstr += str(iterator.data) + '--->'
            '''following the link in linked list and iterating through one by one'''
            iterator = iterator.next
        print(llstr)

print()
if __name__ == '__main__':
    '''creating linked list object'''
    ll1 = LinkedList()
    '''inserts 5 and then 89b at the beginning'''
    '''Debug program to see how inserting at beginning works (break at if statement)'''
    ll1.insert_at_beginning(5)
    ll1.insert_at_beginning(89)
    '''inserting 79 at the end of linked list'''
    ll1.insert_at_end(79)
    ll1.insert_at_end(1)
    ll1.insert_at_end(9839)
    ll1.print()

    ll2 = LinkedList()
    '''inserting whole list of data at the end of a blank linked list'''
    ll2.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll2.print()
    '''printing the length of linked list'''
    print("length", ll2.get_length())
    '''removing element in linked list at specific index'''
    ll2.remove_at(2)
    '''raises an exception because index out of bounds'''
    # ll2.remove_at(-2)
    ll2.print()
    '''insert elments at index and specifying element'''
    ll2.insert_at(0, 'figs')
    ll2.print()
    ll2.insert_at(2, 'jackfruit')
    ll2.print()

print()
    
