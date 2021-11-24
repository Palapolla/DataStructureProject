# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = Node(None, None, None)
#         self.tail = Node(None, self.head, None)
#         self.head.next = self.tail
#         self.size = 0

#     def __str__(self):
#         curr = self.head.next
#         s = ""
#         while curr is not self.tail:
#             s += str(curr.data) + " < - > "
#             curr = curr.next

#         if s == "":
#             return ""
#         else:
#             return s

#     def __len__(self):
#         return self.size()

#     # def str_reverse(self):
#     #     curr = self.tail.prev
#     #     s = ""
#     #     while curr is not self.head:
#     #         s += str(curr.data) + " "
#     #         curr = curr.prev

#     #     if s == "":
#     #         return ""
#     #     else:
#     #         return "->".join(s.split())

#     def isEmpty(self):
#         return self.size == 0

#     def append(self, data):
#         NewNode = Node(data)
#         NewNode.next = None
#         if self.head is None:
#             NewNode.prev = None
#             self.head = NewNode
#             print('1')
#             self.size +=1
#             return
#         last = self.head
#         while (last.next is not None):
#             last = last.next
#         last.next = NewNode
#         NewNode.prev = last
#         print('2')
#         self.size +=1
#         return
#         # if self.isEmpty():
#         #     newNode = Node(data)
#         #     self.head = newNode
#         #     self.tail = newNode
#         #     self.size += 1
#         # else:
#         #     newNode = Node(data, self.tail.prev, self.tail)
#         #     self.tail.prev.next = newNode
#         #     self.tail.prev = newNode
#         #     self.size += 1

#     def insert(self, index, data):
#         if index >= 0 and index <= self.size:
#             curr = self.head
#             for i in range(index):
#                 curr = curr.next
#             newNode = Node(data, curr, curr.next)
#             curr.next.prev = newNode
#             curr.next = newNode
#             self.size += 1
#         else:
#             print("Data cannot be added")

#     def index(self, value):
#         p = self.head
#         count = 0
#         while p is not None:
#             if p.value == value:
#                 return count
#             count += 1
#             p = p.next
#         return -1
    
#     def get(self, index):
#         if not self.isEmpty():
#             if index > self.size-1:
#                 print('out of range')
#                 return
#             else:
#                 p = self.head
#                 print(self.head.data)
#                 for i in range(index+1):
#                     p = p.next
#                     print('p ',p.data)
#                 return p

#     def remove(self, data):
#         try:
#             index = -1
#             curr = self.head
#             while curr.data != data:
#                 index += 1
#                 curr = curr.next
#             curr.prev.next = curr.next
#             curr.next.prev = curr.prev
#             self.size -= 1
#             print("removed : {} from index : {}".format(data, index))
#         except AttributeError:
#             print("Not Found!")




# ref. https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Create the doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

# Define the push method to add elements at the begining
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

# Define the append method to add elements at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            self.size += 1
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        self.size += 1
        return
    
    def get(self,index):
        if self.head is None:
            print("linked list is empty")
            return
        if self.size < index:
            print('out of range')
            return
        curr = self.head
        for ind in range(index):
            curr = curr.next
        return curr

    def __str__(self):
        curr = self.head.next
        s = ""
        while curr is not None:
            s += str(curr.data) + " < - > "
            curr = curr.next

        if s == "":
            return ""
        else:
            return s
    
    def __len__(self):
        return self.size
        

# Define the method to print
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next
