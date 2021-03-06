# Now modify print_tree method to take tree level as input. 
# And that should print tree only up to that level

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        spaces = ' ' * self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        nodeLevel = self.get_level()
        if nodeLevel <= level:
            print(prefix + self.data)
        # if self.data == "Palo Alto":
        #     print(nodeLevel, level)
        if self.children:
            for child in self.children:
                child.print_tree(level)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_location_tree():
        globalTree = TreeNode("Global")

        india = TreeNode("India")
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
        usa.add_child(jersey)
        jersey.add_child(TreeNode("Priceton"))
        jersey.add_child(TreeNode("Trenton"))
        cali = TreeNode("California")
        usa.add_child(cali)
        cali.add_child(TreeNode("San Francisco"))
        cali.add_child(TreeNode("Mountain View"))
        paloAlto = TreeNode("Palo Alto")
        cali.add_child(paloAlto)
        

        globalTree.add_child(india)
        globalTree.add_child(usa)

        return globalTree

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(2)