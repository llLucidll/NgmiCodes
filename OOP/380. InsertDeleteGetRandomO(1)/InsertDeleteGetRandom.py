import random 
class RandomizedSet:
    def __init__(self):
        self.cache = []
        self.memory = {}

    def insert(self, val: int) -> bool:
        if val in self.memory:
            return False 
        
        self.memory[val] = len(self.cache)
        self.cache.append(val)
        return True    
    
    def remove(self, val: int) -> bool:
        if val not in self.memory:
            return False

        # First we get the last index and the last val from the array 
        last_idx = len(self.cache) - 1
        last_val = self.cache[last_idx]
        idx = self.memory[val]

        # replacing the idx with the last_val
        self.memory[last_val] = idx 
        self.cache[idx] = last_val

        # Removing the old entries
        del self.memory[last_val]
        self.cache.pop()
        return True 
    
    def getRandom(self):
        return self.cache[random.randrange(len(self.cache))]