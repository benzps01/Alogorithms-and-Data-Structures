'''
Implementation of Binary Search Tree
Methods include:

in_order, pre_order and post_order traversals using recursion
search if an element exists
finding min and max value in the tree
calculating the sum of all the nodes in the BST
'''
class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTreeNode(data)
        else:
            # add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base Node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    '''def InOrder(root):
        current = root
        stack = []

        while True:

            if current is not None:
                stack.append(current)

                current = current.left
            
            elif(stack):
                current = stack.pop()
                print(current.data, end=" ")

                current = current.right
            
            else:
                break
'''

    def pre_order_traversal(self):
        elements = []

        #visit base Node
        elements.append(self.data)

        #visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        #visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        #visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        #visit base Node
        elements.append(self.data)
    
        return elements


    

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            #value might be in left subtree
            if self.left:
                #recursive function
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left

        return current.data

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        
        return current.data

    def calculate_sum(self):
        if self.left:
            left = self.left.calculate_sum()
        else:
            left = 0
        
        if self.right:
            right = self.right.calculate_sum()
        else:
            right = 0

        return self.data + left + right


def build_tree(elements):
    root = BSTreeNode(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34,18,4]
    root = numbers[0]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(34))
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.calculate_sum())
    #print(numbers_tree.InOrder(root))

'''
    countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print('UK is in the list? ', country_tree.search("UK"))
    print("Sweden is in the list? ",country_tree.search("Sweden"))
    print(country_tree.in_order_traversal())
    print(country_tree.find_min())
    print(country_tree.find_max())'''