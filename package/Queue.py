class Queue:
    def __init__(self):
        self.items = list()

    def enQueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.size() <= 0

    def deQueue(self):
        if not self.is_Empty():
            return self.items.pop(0)
        else:
            return 'Empty'

    def __str__(self):
        output = ""
        if not self.is_Empty():
            for item in range(len(self.items)):
                output += str(self.items[item])
                if item < len(self.items)-1:
                    output += ', '
        else:
            output = 'Empty'
        return output