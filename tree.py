'''
Implementation of a basic Tree data structure
with 2 exercises
'''
class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children):   # this section is for recursive calling of the print tree function so that the child nodes can be printed
            for child in self.children:
                child.print_tree()
        

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
    

if  __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()

'''
### Exercise 1:

Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

class TreeNode:

    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,info):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if info == 'name':
            print(prefix + self.name)
        elif info == 'designation':
            print(prefix + " ("+ self.designation + ")" )
        elif info == 'both':
            print(prefix + self.name + " ("+ self.designation + ")")
        if len(self.children):
            for child in self.children:
                child.print_tree(info)
    

def build_employee_tree():
    root_name = TreeNode("Nilupal","CEO")

    man1 = TreeNode("Chinmay","CTO")
    man2 = TreeNode("Gels","HR Head")

    sman1 = TreeNode("Vishwa","Infrastructure Head")
    sman2 = TreeNode("Aamir","Application Head")
    sman3 = TreeNode("Peter","Recruitment Manager")
    sman4 = TreeNode("Waqas","Policy Manager")

    emp1 = TreeNode("Dhaval","Cloud Manager")
    emp2 = TreeNode("Abhijit","App Manager")

    sman1.add_child(emp1)
    sman1.add_child(emp2)

    man1.add_child(sman1)
    man1.add_child(sman2)

    man2.add_child(sman3)
    man2.add_child(sman4)

    root_name.add_child(man1)
    root_name.add_child(man2)

    return root_name



if __name__ == '__main__':
    root_node = build_employee_tree()
    root_node.print_tree('name')
    print(" ")
    root_node.print_tree('designation')
    print(" ")
    root_node.print_tree('both')'''



'''
### Exercise 2
Now modify print_tree method to take tree level as input. And that should print tree only upto that level

class TreeNode:

    def __init__(self,location):
        self.location = location
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.location)
        if len(self.children):
            for child in self.children:
                child.print_tree(level)

def build_gloc_tree():
    root = TreeNode("Global")

    country1 = TreeNode("India")

    state1 = TreeNode('Gujrat')
    city1 = TreeNode('Ahmedabad')
    city2 = TreeNode('Baroda')
    state1.add_child(city1)
    state1.add_child(city2)

    state2 = TreeNode('Karnataka')
    city3 = TreeNode('Bangluru')
    city4 = TreeNode('Mysore')
    state2.add_child(city3)
    state2.add_child(city4)

    country1.add_child(state1)
    country1.add_child(state2)


    country2 = TreeNode("USA")

    state3 = TreeNode('New Jersey')
    city5 = TreeNode('Princeton')
    city6 = TreeNode('Trenton')
    state3.add_child(city5)
    state3.add_child(city6)

    state4 = TreeNode('California')
    city7 = TreeNode('San Francisco')
    city8 = TreeNode('Mountain View')
    city9 = TreeNode('Palo Alto')
    state4.add_child(city7)
    state4.add_child(city8)
    state4.add_child(city9)

    country2.add_child(state3)
    country2.add_child(state4)

    root.add_child(country1)
    root.add_child(country2)

    return root

if  __name__ == '__main__':
    root = build_gloc_tree()
    root.print_tree(2)'''
    