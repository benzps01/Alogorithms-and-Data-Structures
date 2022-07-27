'''
This is an example of a Data Structure --> Doubly Linked List
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
12. print forward
13. print backward
'''

class Element:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DLL:
    def __init__(self):
        self.head = None

    def InsertBegin(self,new_data):
        new_node = Element(new_data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def InsertEnd(self, new_data):
        new_node = Element(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr

    def InsertAfter(self,data,after_data):
        itr = self.head
        if itr == None:
            print('The node is not present here')
        else:
            while itr is not None:
                if itr.data == after_data:
                    break
                itr = itr.next
            new_node = Element(data)
            new_node.prev = itr
            new_node.next = itr.next
            if itr.next is not None:
                itr.next.prev = new_node
            itr.next = new_node

    def InsertBefore(self,data,before_data):
        itr = self.head
        if itr == None:
            return 'There is no such node'
        else:
            while itr:
                if itr.data == before_data:
                    break
                itr = itr.next
            new_node = Element(data)
            new_node.prev = itr.prev
            new_node.next = itr
            if itr.prev is not None:
                itr.prev.next = new_node
            itr.prev = new_node

    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.InsertEnd(data)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.InsertBegin(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                break
            itr = itr.next
            count += 1
        new_node = Element(data)
        new_node.prev = itr
        new_node.next = itr.next
        if itr.next is not None:
            itr.next.prev = new_node
        itr.next = new_node

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next.next.prev = itr
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
            itr = itr.next
            count += 1

    def search(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                break
            itr = itr.next
            count += 1
        print(f'Data at {count} is: ',itr.data)


    def printforward(self):
        lstr = ''
        temp = self.head
        while (temp):
            lstr += str(temp.data) + " --> "
            temp = temp.next
        print('')
        print(lstr)
        print('')

    def printbackward(self):
        lstr = ''
        count = doublyll.get_length()
        itr = doublyll.get_position(count-1)
        while itr:
            lstr += str(itr.data) + " --> "
            itr = itr.prev
        print('')
        print(lstr)
        print('')

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

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
                return itr
            itr = itr.next
            count += 1
        return None
        

##Calling the methods
doublyll = DLL()  ## creating ll object / empty list
##Creating 3 nodes
doublyll.head = Element(1)  
second = Element(2)
third = Element(3)

##Linking the 3 nodes to next
doublyll.head.next = second
doublyll.head.prev = None
second.next = third
second.prev = doublyll.head
third.prev = second

doublyll.InsertBegin(0)
doublyll.InsertEnd(9)
doublyll.printforward()
print("Length of the Doubly Linked List: ", doublyll.get_length())
doublyll.get_position(4)
doublyll.printbackward()
print('Insert After')
doublyll.InsertAfter(4,3)
doublyll.printforward()
doublyll.printbackward()

print('Insert At')
doublyll.insert_at(2,10)
doublyll.printforward()
doublyll.printbackward()

print('Insert Before')
doublyll.InsertBefore(6,10)
doublyll.printforward()
doublyll.printbackward()

print('Insert Muliple values')
doublyll.insert_values([9,11,20,30])
doublyll.printforward()
doublyll.printbackward()

print('Remove At')
doublyll.remove_at(4)
doublyll.printforward()
doublyll.printbackward()

print('Remove By Value')
doublyll.remove_by_value(11)
doublyll.printforward()
doublyll.printbackward()

doublyll.search(9)