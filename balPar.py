from sys import argv

script, strin = argv

strin = str(strin)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)
    
    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

def main(strin):
    s = Stack()
    balanced = True
    index = 0
    while index < len(strin) and balanced:
        symbol = strin[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        
        index += 1
    
    if balanced and s.isEmpty():
        print(strin)
        return True
    else: 
        print(strin)
        return False

print(main(strin))
