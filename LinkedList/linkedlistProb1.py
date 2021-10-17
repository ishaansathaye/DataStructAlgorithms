'''1. Add following methods to linked list class'''
# def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
#     # Remove first node that contains data

'''Make the following calls: '''
# ll = LinkedList()
# ll.insert_values(["banana","mango","grapes","orange"])
# ll.print()
# ll.insert_after_value("mango","apple") # insert apple after mango
# ll.print()
# ll.remove_by_value("orange") # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iteration = self.head
        while iteration:
            count += 1
            iteration = iteration.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iteration = self.head
        while iteration:
            if count == (index-1):
                iteration.next = iteration.next.next
                break
            iteration = iteration.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        iteration = self.head
        while iteration:
            if count == (index-1):
                node = Node(data, iteration.next)
                iteration.next = node
                break
            iteration = iteration.next
            count += 1
    
    '''made function'''
    def insert_after_value(self, data_after, data_to_insert):
        #need to to check if empty too
        if self.head == None:
            return

        iteration = self.head
        while iteration:
            if iteration.data == data_after:
                node = Node(data_to_insert, iteration.next)
                iteration.next = node
                break
            iteration = iteration.next
    
    '''made function'''
    def remove_by_value(self, data):
        #need to check if empty too
        if self.head == None:
            return

        iteration = self.head
        count = 0
        while iteration:
            if iteration.data == data:
                self.remove_at(count)
                break
            iteration = iteration.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        iterator = self.head
        llstr = ''
        while iterator:
            llstr += str(iterator.data) + '--->'
            iterator = iterator.next
        print(llstr)

print()
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

print()
    
