from traceback import print_stack


class Stack(object):
    min = float('inf')
    
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, x):
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    
    def pop(self):
        temp = self.stack[-1]
        self.stack.pop()
        if self.min == temp:
            self.min = self.stack[-1]
            self.stack.pop()
    
    def top(self):
        try:
            if self.count == 0:
                raise Exception("Stack is Empty, returning None")
            return self.stack[-1]
        except Exception as e:
            print(str(e))
    
    def getMin(self):
        return self.min

    def count(self):
        return len(self.stack)

    def printStack(stack):
        temp = Stack()  # create a temp stack to hold the values of original stack
        while (stack.count() > 0):
            temp.push(stack.top())
            stack.pop()
        
        while(temp.count() > 0):
            x = temp.top()
            print("{} ".format(x), end = "")
            temp.pop()
            stack.push(x) # restores the original stack


test = Stack()
test.push(34)
test.push(18)
test.push(29)
test.push(91)
test.push(736)
test.push(53)
test.push(177)
test.push(5)
print("Stack: ")
test.printStack()
print("\nTesting pop. The last element (5) should be removed.")
test.pop()
print("Stack: ")
test.printStack()
print("\nTesting min")
print("Minimum is: " + str(test.getMin()))