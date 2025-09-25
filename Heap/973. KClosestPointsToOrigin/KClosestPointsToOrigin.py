import heapq
def distance(coord: list[int]) -> int:
    x, y = coord[0], coord[1]
    return (x**2 + y**2)

def kClosest(points: list[int], k: int) -> list[int]:
    minHeap = []
    for point in points:
        minHeap.append([distance(point), point])
    
    heapq.heapify(minHeap)
    res = []
    while k > 0:
        res.append(heapq.heappop(minHeap)[1])
        k -= 1
    return res