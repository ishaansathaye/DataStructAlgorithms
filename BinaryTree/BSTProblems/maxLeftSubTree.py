# 1. Modify delete method in class BinarySearchTreeNode class to use max element from left subtree. 
# You will remove lines marked with ---> and use max value from left subtree
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def breadth_first_traversal(self):
        elements = []
        traversed = []
        
        if self.data:
            elements.append(self.data)
            traversed.append(self)
        while traversed:
            base = traversed.pop(0)
            if base.left:
                elements.append(base.left.data)
                traversed.append(base.left)
            if base.right:
                elements.append(base.right.data)
                traversed.append(base.right)
        
        return elements

    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            #NOTE: case 3: node with 2 children
            #Alternate Approach (2): Finding Max of Left Subtree
            maxValue = self.left.find_max() #find maximum from left subtree
            self.data = maxValue #copy maximum 
            self.left = self.left.delete(maxValue) #returns a new subtree by deleting duplicate
        
        return self

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        
        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()

        return sum

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)): 
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print("Original Elements:", numbers_tree.in_order_traversal())
    numbers_tree.delete(20) #can also verify using debugger
    print("Case#3-Deleted 20:", numbers_tree.in_order_traversal())

    print()

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print("Original Elements:", numbers_tree.in_order_traversal())
    numbers_tree.delete(23)
    print("Case#2-Deleted 23:", numbers_tree.in_order_traversal())

    print()

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print("Original Elements:", numbers_tree.in_order_traversal())
    numbers_tree.delete(9)
    print("Case #1-Deleted 9:", numbers_tree.in_order_traversal())

    print()