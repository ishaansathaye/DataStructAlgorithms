#Binary Search Tree: values are in order with less than root node being left subtree and greater than root node being right subtree
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: #if the value already exists
            return
        
        if data < self.data: #if value less than current node then add data in left subtree
            if self.left: #if current node has a left node then it is not a leaf node
                self.left.add_child(data) #use recursion on the left subtree of current node
            else:
                self.left = BinarySearchTreeNode(data)
        else: #if value greater than current node then add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self): #traverse left tree, then base node, then right subtree
        elements = []

        #traverse left tree
        if self.left:
            elements += self.left.in_order_traversal() #use recursion to keep going to leftmost node of left subtree and adding to list

        #traverse base node
        elements.append(self.data)

        #traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements #returns elements in an ascending order

    def search(self, value): #searching for a value
        if self.data == value:
            return True
        
        if value < self.data: #value might be in left subtree
            if self.left:
                return self.left.search(value) #use recursion to further go into left subtree
            else: #if there is no left children of the base node
                return False

        if value > self.data: #might be in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) #creates a root node 

    for i in range(1, len(elements)): 
        root.add_child(elements[i]) #adding all children and sub-children to root node
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4] #only will include unique values
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print()
    print(numbers_tree.search(20))