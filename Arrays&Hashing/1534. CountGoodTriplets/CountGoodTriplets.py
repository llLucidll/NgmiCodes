def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    max = len(arr)
    current = 0

    for i in range(max):
        for j in range(i + 1, max):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j + 1, max):
                if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                    current += 1

    
    return current