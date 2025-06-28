"""
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""

class MinStack:
    def __init__(self):
        # Intialize the storage and the current minimum
        self.cache = []
        self.min = float("inf")
    def push(self, val: int):
        # If we dont have any values, then we initialize the minimum
        if not self.cache:
            self.min = val
            self.cache.append(0) #The difference is 0
        else:
            # Update the minimum if its lesser
            self.cache.append(val - self.min)
            if val < self.min:
                self.min = val
    def pop(self):
        if not self.stack:
            return
        
        pop = self.stack.pop()
        if pop < 0:
            self.min -= pop # Change our minimum by the value.
        
    def top(self):
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def get_min(self):
        return self.min
