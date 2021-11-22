# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        '''Can also check for duplicate child elements here'''
        child.parent = self
        self.children.append(child)

    def print_tree(self, option):
        spaces = ' ' * self.get_level()*3
        '''Checks if current node has a parent and then adds format'''
        prefix = spaces + "|__" if self.parent else ""
        if option == 'name':
            print(prefix + self.data)
        elif option == 'designation':
            print(prefix + self.designation)
        elif option == 'both':
            print(prefix + self.data + " " + "("+self.designation+")")
        else:
            print('Not an option.')
        '''if children do exist'''
        if self.children:
            for child in self.children:
                child.print_tree(option)
    
    def get_level(self):
        level = 0
        p = self.parent
        '''if parent does exist'''
        while p:
            level += 1
            p = p.parent
        return level


def build_management_tree():
        ceo = TreeNode("Nilupul", "CEO")

        cto = TreeNode("Chinmay", "CTO")
        infraHead = TreeNode("Vishwa", "Infrastructure Head")
        cto.add_child(infraHead)
        infraHead.add_child(TreeNode("Dhaval", "Cloud Manager"))
        infraHead.add_child(TreeNode("Abhijit", "App Manager"))
        cto.add_child(TreeNode("Aamir", "Application Head"))
        
        hrHead = TreeNode("Gels", "HR Head")
        hrHead.add_child(TreeNode("Peter", "Recruitment Manager"))
        hrHead.add_child(TreeNode("Waqas", "Policy Manager"))

        ceo.add_child(cto)
        ceo.add_child(hrHead)

        return ceo

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy