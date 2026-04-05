class MinStack:

    def __init__(self):
        self.stack = list()
        self.minStack = list()
        self.minStack.append(10**10)

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(self.minStack)
        return self.minStack[-1]
