def topKFrequent(nums, k:int):
    count = {}
    # Create the buckets
    freq = [[] for i in range(len(nums) + 1)]
    result = []

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    for num, cnt in count.items():
        freq[cnt].append(num)
    
    for i in range(len(freq) - 1, -1, -1):
        for num in freq[i]:
            result.append(num)

            if len(result) == k:
                return result
            