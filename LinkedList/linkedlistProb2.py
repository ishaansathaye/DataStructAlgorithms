'''2. Implement a double linked list.'''
'''Add following new methods'''
# def print_forward(self):
#     # This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
#     def __init__(self):
#         self.head = None 
    
#     def insert_at_beginning(self, data):
#         if self.head == None:
#             node = Node(data, self.head, None)
#             self.head = node
#         else:
#             node = Node(data, self.head, None)
#             self.head.prev = node
#             self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data, None, iterator)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

#     def get_length(self):
#         count = 0
#         iterator = self.head
#         while iterator:
#             count += 1
#             iterator = iterator.next
#         return count

#     def remove_at(self, index):
#         if index < 0 or index >= self.get_length():
#             raise Exception("Invalid index")
        
#         if index == 0:
#             self.head = self.head.next
#             self.head.prev = None
#             return
        
#         count = 0
#         iterator = self.head
#         while iterator:
#             if count == index:
#                 iterator.prev.next = iterator.next
#                 if iterator.next:
#                     iterator.next.prev = iterator.prev
#                 break
#             iterator = iterator.next
#             count += 1
    
#     def insert_at(self, index, data):
#         if index < 0 or index >= self.get_length():
#             raise Exception("Invalid index")
        
#         if index == 0:
#             self.insert_at_beginning(data)
#             return
        
#         count = 0
#         iteration = self.head
#         while iteration:
#             if count == (index-1):
#                 node = Node(data, iteration.next, iteration)
#                 if node.next:
#                     node.next.prev = node
#                 iteration.next = node
#                 break
#             iteration = iteration.next
#             count += 1

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        iterator = self.head
        listLinkedElements = ''
        while iterator:
            listLinkedElements += str(iterator.data) + '--->'
            iterator = iterator.next
        print(listLinkedElements)
    # This method prints list in forward direction. Use node.next

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # last_node = self.get_last_node()
        # iterator = last_node
        iterator = self.head
        listLinkedElements = ''
        while iterator.next:
            iterator = iterator.next
        if iterator:
            while iterator:
                listLinkedElements += str(iterator.data) + '--->'
                iterator = iterator.prev
            print("Link List is reverse:", listLinkedElements)
    # Print linked list in reverse direction. Use node.prev for this.

#     def get_last_node(self):
#         iterator = self.head
#         while iterator.next:
#             iterator = iterator.next
#         return iterator

class Node2:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList2:
    # def __init__(self):
    #     self.head = None 

    # def insert_at_beginning(self, data):
    #     node = Node(data, self.head)
    #     self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node2(data, None, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node2(data, None, iterator)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # def get_length(self):
    #     count = 0
    #     iteration = self.head
    #     while iteration:
    #         count += 1
    #         iteration = iteration.next
    #     return count

    # def remove_at(self, index):
    #     if index < 0 or index >= self.get_length():
    #         raise Exception("Invalid index")
        
    #     if index == 0:
    #         self.head = self.head.next
    #         return
        
    #     count = 0
    #     iteration = self.head
    #     while iteration:
    #         if count == (index-1):
    #             iteration.next = iteration.next.next
    #             break
    #         iteration = iteration.next
    #         count += 1
    
    # def insert_at(self, index, data):
    #     if index < 0 or index >= self.get_length():
    #         raise Exception("Invalid index")
        
    #     if index == 0:
    #         self.insert_at_beginning(data)
    #         return
        
    #     count = 0
    #     iteration = self.head
    #     while iteration:
    #         if count == (index-1):
    #             node = Node(data, iteration.next)
    #             iteration.next = node
    #             break
    #         iteration = iteration.next
    #         count += 1

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        iterator = self.head
        llstr = ''
        while iterator:
            llstr += str(iterator.data) + '--->'
            iterator = iterator.next
        print(llstr)

    def print_backward(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        iterator = self.head
        llstr = ''
        while iterator:
            iterator = iterator.next
        while iterator:
            llstr += str(iterator.data) + '--->'
            iterator = iterator.prev
        print(llstr)
    # Print linked list in reverse direction. Use node.prev for this.

print()
if __name__ == '__main__':
    dll = DoubleLinkedList2()
    dll.insert_values(["banana","mango","grapes","orange"])
    dll.print_forward()
    dll.print_backward()
    # dll.insert_at_end("figs")
    # dll.print_forward()
    # dll.insert_at(0,"jackfruit")
    # dll.print_forward()
    # # dll.insert_at(6,"dates")
    # # dll.print_forward()
    # dll.insert_at(2,"kiwi")
    # dll.print_forward()

print()
    
