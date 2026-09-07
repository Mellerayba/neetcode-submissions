class MinStack:
    
    def __init__(self):
        self.stack = []
        self.smallest = []
    def push(self, val: int) -> None:
        if self.smallest:
            self.smallest.append(min(self.smallest[-1],val))
        else:
            self.smallest.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.smallest = self.smallest[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.smallest[-1]
