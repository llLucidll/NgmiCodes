import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.data = nums
        self.k = k 
        heapq.heapify(self.data)
        while len(self.data) > self.k:
            heapq.heappop(self.data)
        
    
    def add(self, val:int):
        heapq.heappush(self.data, val)
        while len(self.data) > self.k:
            heapq.heappop(self.data)
        
        return self.data[0]