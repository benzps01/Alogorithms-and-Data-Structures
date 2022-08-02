'''
Implementation of Binary Search Tree
Methods include:

in_order, pre_order and post_order traversals using recursion
search if an element exists
finding min and max value in the tree
calculating the sum of all the nodes in the BST
added delete a node from the tree
'''
from requests import delete


class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, root):
        if root is None:
            self.data == root
            return 

        if root == self.data:
            return
        
        if root < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(root)
            else:
                self.left = BSTreeNode(root)
        else:
            # add data to right subtree
            if self.right:
                self.right.add_child(root)
            else:
                self.right = BSTreeNode(root)

# This is based on Recursive Method
    def in_order_traversal(self,root):
        '''
        Method 1
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base Node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements'''

        '''
        Method 2
        '''
        if root is None:
            return []
        return self.in_order_traversal(root.left) + [root.data] + self.in_order_traversal(root.right)


#This is based on Iterative Method
    def InOrder(self,root):

        stack = []
        current = root
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data, end  = " ")
                current = current.right

        print()


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

    def PreOrder(self,root):
        stack = []
        current = root
        while stack or current:
            while current:
                print(current.data,end = " ")
            
                if current.right:
                    stack.append(current.right)

                current = current.left

            if stack:
                current = stack.pop()

        print()

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

    def PostOrder(self,root):
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                stack.append(current)
                current = current.left

            if stack is None:
                return
            
            current = stack.pop()

            if stack and stack[-1] == current:
                current = current.right
            else:
                print(current.data,end=" ")
                current = None

        print()


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

    def delete(self, val):
        if self.data is None:
            return None
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return None
            if self.right is None:
                temp = self.left
                self = None
                return None
            current = self.right
            while current.left:
                current = current.left
            self.data = current.data
            self.right = self.right.delete(current.data)
        return self


            

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

countries = [17,4,1,20,9,23,18,34,18,4]
#countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
root = BSTreeNode(countries[0])
for i in countries:
    root.add_child(i)
    #numbers_tree = build_tree(numbers)
print(root.search(34))
print(root.in_order_traversal(root))
print(root.pre_order_traversal())
print(root.post_order_traversal())
print(root.find_max())
print(root.find_min())
print(root.calculate_sum())
root.InOrder(root)
root.PreOrder(root)
root.PostOrder(root)

root.add_child(3)
root.InOrder(root)
root.delete(17)
print(root.data)
root.InOrder(root)


'''
    countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print('UK is in the list? ', country_tree.search("UK"))
    print("Sweden is in the list? ",country_tree.search("Sweden"))
    print(country_tree.in_order_traversal())
    print(country_tree.find_min())
    print(country_tree.find_max())'''