import heapq 

def lastStoneWeight(self, stones: list[int]) -> int:
    #Declaring our max heap
    heap = [-1 * x for x in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        s1 = -1 * heapq.heappop(heap)
        s2 = -1 * heapq.heappop(heap)

        if s1 == s2:
            continue
        else:
            s3 = s1 - s2
            heapq.heappush(heap, -1 * s3)
    
    
    if not heap:
        return 0
    else:
        return -1 * heap[0]