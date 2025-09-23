<<<<<<< HEAD
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
=======
import heapq
def lastStoneWeight(stones: list[int]) -> int:
    maxHeap = []

    for stone in stones:
        heapq.heappush(maxHeap, -stone)

    while len(maxHeap) >= 2:
        stone1 = -heapq.heappop(maxHeap)
        stone2 = -heapq.heappop(maxHeap)

        if stone1 != stone2:
            heapq.heappush(maxHeap, -abs(stone1 - stone2))


    if maxHeap:
        return -maxHeap[0]
    else:
        return 0
>>>>>>> fe010a1 (Solved 1929. ConcatenationOfArray)
