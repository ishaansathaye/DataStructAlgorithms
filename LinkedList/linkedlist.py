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

if __name__ == '__main__':
    '''creating linked list object'''
    ll = LinkedList()
    '''inserts 5 and then 89b at the beginning'''
    '''Debug program to see how inserting at beginning works'''
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()
