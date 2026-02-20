def shortestWord(wordsDict, word1, word2):
    shortest = float("inf")
    curr = None
    
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            if curr != None and wordsDict[curr] == word2 and curr != i:
                shortest = min(shortest, abs(i - curr))
            curr = i
        elif wordsDict[i] == word2:
            if curr != None and wordsDict[curr] == word1 and curr != i:
                shortest = min(shortest, abs(i - curr))
            curr = i
    
    return shortest
