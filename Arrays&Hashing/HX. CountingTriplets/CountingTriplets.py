def countTriplets(arr, d: int) -> int:
    # Do our first pass:
    arr = [x % d for x in arr]

    #pairCount has the length = d
    pairCount = [0] * d 
    result = 0

    for i in range(len(arr)):
        # Check if we have a triplet
        lookup = (d - arr[i]) % d
        if pairCount[lookup] >= 1:
            # we add pairCount[lookup] as thats the number of pairs we can add current element to to make a good triplet.
            result += pairCount[lookup]
        
        for j in range(0, i):
            # Update pairCount
            curr = arr[i] + arr[j]
            curr = curr % d
            pairCount[curr] += 1
    
    return result


