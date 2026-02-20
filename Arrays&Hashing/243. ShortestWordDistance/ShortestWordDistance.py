def shortestDistance(wordsDict, word1, word2):
    shortest = float("inf")
    curr = None

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1 or wordsDict[i] == word2:
            if curr != None and wordsDict[curr] != wordsDict[i]:
                shortest = min(shortest, i - curr)
            curr = i
    
    return shortest