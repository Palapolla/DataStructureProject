class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'Value in Stack = '
        if self.isEmpty():
            return s+"Empty"
        else:
            for ele in self.items:
                s += str(ele)+' '
            return s
    def push(self, i):
        self.items.append(i)
        return "Add = "+str(i)+" and Size = "+str(self.size())

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            s = "Pop = "+str(self.peek())+" and Index = "+str(self.size()-1)
            self.items.pop()
            return  s

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)