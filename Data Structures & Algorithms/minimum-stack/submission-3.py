class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_ele = val
        else:
            if val >= self.min_ele:
                self.stack.append(val)
            else:
                self.stack.append(2*val - self.min_ele)
                self.min_ele = val

        

    def pop(self) -> None:
        if not self.stack:
            return -1
        else:
            if self.stack[-1] >= self.min_ele:
                self.stack.pop()
            elif self.stack[-1] < self.min_ele:
                self.min_ele = 2*(self.min_ele) - self.stack[-1]
                self.stack.pop()
                if not self.stack:
                    self.min_ele = float("inf")
        

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            if self.stack[-1] >= self.min_ele:
                return self.stack[-1]
            else:
                return self.min_ele
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.min_ele
        
