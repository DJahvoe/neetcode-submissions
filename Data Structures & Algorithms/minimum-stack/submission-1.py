class MinStack:

    def __init__(self):
        self.min_val = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_val) == 0:
            self.min_val.append(val)
        else:
            top = self.min_val[-1]
            self.min_val.append(min(top, val))

    def pop(self) -> None:
        self.min_val.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_val[-1]
        
