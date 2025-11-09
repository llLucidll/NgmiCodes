from collections import deque
import heapq 

def leastInterval(tasks: list[int], n: int) -> int:
    
    time = 0
    freq = {}

    for task in tasks:
        freq[task] = 1 + freq.get(task, 0)
    
    maxHeap = [-count for count in freq.values()]
    queue = deque()

    while maxHeap or queue:
        time += 1

        if not maxHeap:
            time = queue[0][1]
        else:
            count = 1 + heapq.heappop(maxHeap)
            if count != 0:
                queue.append([count, time + n])
        
        while queue and queue[0][1] <= time:
            heapq.heappush(maxHeap, queue.popleft()[0])
    
    return time 