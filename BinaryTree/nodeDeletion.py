#Binary Search Tree with Node Deletion
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
                self.left.delete(value) #use recursion to find the node in the left subtree
            else:
                return None #python already does this by default for functions 
        elif value > self.data:
            if self.right:
                self.right.delete(value) ##use recursion to find the node in the right subtree
        else:
            if self.left is None and self.right is None: #case 1: node with no child
                return None
            if self.left is None: #case 2: node with 1 child
                return self.right
            if self.right is None: #case 2: node with 1 child
                return self.left
            
            #Approach 1: Finding Min of Right Subtree (could also implement alternate approach of max of left subtree)
            minValue = self.right.find_min() #find minimum from right subtree
            self.data = minValue #copy minimum 
            self.right = self.right.delete(minValue) #returns a new subtree 
        
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
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())