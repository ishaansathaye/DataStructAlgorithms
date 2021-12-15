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

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    '''TODO: Breadth First Traversal Technique Implementation'''
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

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)): 
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())

    print()

    numbers = [15,12,7,14,27,20,23,88]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.breadth_first_traversal())

    print()

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print(country_tree.search("China"))
    print(country_tree.find_min())
    print(country_tree.find_max())
    print(country_tree.post_order_traversal())
    print(country_tree.pre_order_traversal())