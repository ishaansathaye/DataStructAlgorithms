# Now modify print_tree method to take tree level as input. 
# And that should print tree only up to that level

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        '''Can also check for duplicate child elements here'''
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        spaces = ' ' * self.get_level()*3
        '''Checks if current node has a parent and then adds format'''
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        '''if children do exist'''
        if self.children and self.get_level <= level:
            for child in self.children:
                child.print_tree(level)
    
    def get_level(self):
        level = 0
        p = self.parent
        '''if parent does exist'''
        while p:
            level += 1
            p = p.parent
        return level


def build_location_tree():
        globalTree = TreeNode("Global")

        india = TreeNode("Chinmay")
        gujurat = TreeNode("Gujurat")
        india.add_child(gujurat)
        gujurat.add_child(TreeNode("Ahmedabad"))
        gujurat.add_child(TreeNode("Baroda"))
        karnataka = TreeNode("Karnataka")
        india.add_child(karnataka)
        karnataka.add_child(TreeNode("Bangluru"))
        karnataka.add_child(TreeNode("Mysore"))
        
        usa = TreeNode("USA")
        jersey = TreeNode("New Jersey")
        india.add_child(gujurat)
        gujurat.add_child(TreeNode("Ahmedabad"))
        gujurat.add_child(TreeNode("Baroda"))
        cali = TreeNode("Karnataka")
        india.add_child(karnataka)
        karnataka.add_child(TreeNode("Bangluru"))
        karnataka.add_child(TreeNode("Mysore"))
        

        globalTree.add_child(india)
        globalTree.add_child(usa)

        return globalTree

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(1)