'''
This is an example of a Data Structure --> Linked List
The methods implemented are :
1. Insert Beginning
2. Insert End
3. Insert After a value
4. Insert Before a value
5. Insert Multiple Values
6. Insert at a particular point
7. Remove a value at an index
8. remove by the value
9. searching through the linked list and returning the location
10. getting the length of the linked list
11. getting the value at the position
'''

##Creating class Element
from turtle import position


class Element:

    ##Initializing the Element object
    def __init__(self,data):
        self.data = data ##Assign data
        self.next = None ## Initialize next node as Null

##Linked List object
class LinkedList:

    def __init__(self):
        self.head = None ##Initializing head i.e the starting point of LL

    ## insert calues at the beginning of llist
    def InsertBegin(self, new_data):
        new_node = Element(new_data)
        new_node.next = self.head
        self.head = new_node

    def InsertEnd(self, new_data):
        new_node = Element(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head
            while (last.next):
                last = last.next
            last.next = new_node

    def InsertAfter(self, data, x):
        n = self.head
        while n:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print('Node is not present is LL')
        else:
            new_node = Element(data)
            new_node.next = n.next
            n.next = new_node
        
    def InsertBefore(self,new_data,before_value):
        if self.head is None:
            raise Exception ("Linked List is empty")
        if self.head.data == before_value:
            new_node = Element(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        itr = self.head
        while itr.next is not None:
            if itr.next.data == before_value:
                break
            itr = itr.next
        if itr.next is None:
            print('Node is not found')
        else:
            new_node = Element(new_data)
            new_node.next = itr.next
            itr.next = new_node
            

    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.InsertEnd(data)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.InsertBegin(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Element(data)
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if data_after == itr.data:
                new_node = Element(data_to_insert)
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            count += 1

        
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_by_value(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            itr = itr.next
            count += 1

    def search(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                break
            else:
                itr = itr.next
                count += 1
        print(f"Data exists at {count}")

    ##printing the ll
    def printList(self):
        lstr = ''
        temp = self.head
        while (temp):
            lstr += str(temp.data) + " --> "
            temp = temp.next
        print('')
        print(lstr)
        print('')

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_position(self, position):
        count = 0
        itr = self.head
        while itr:
            if count == position:
                print(itr.data)
            itr = itr.next
            count += 1
        return None

llist = LinkedList()  ## creating ll object / empty list

##Creating 3 nodes
llist.head = Element(1)  
second = Element(2)
third = Element(3)

llist.insert_values([9,10,20,30])
##Linking the 3 nodes to next
llist.head.next = second
second.next = third

llist.InsertBegin(0)
llist.InsertEnd(4)
llist.InsertEnd(6)
llist.insert_values([9,10,20,30])
llist.InsertAfter(5,4)
llist.printList()
print('Length: ',llist.get_length())
llist.insert_at(9,33)
print('Length: ',llist.get_length())
llist.printList()
llist.remove_at(8)
print('Length: ',llist.get_length())
llist.insert_after_value(5,88)
llist.printList()
print('Length: ',llist.get_length())
llist.printList()
print('Length: ',llist.get_length())
llist.get_position(6)
llist.remove_by_value(88)
print('Length: ',llist.get_length())
llist.printList()

llist.search(33)

llist.InsertBefore(10,33)
llist.printList()
print('Length: ',llist.get_length())
