from collections import defaultdict
class WordDistance:
    def __init__(self, wordsDict):
        self.locations = defaultdict(list)

        for i in range(len(wordsDict)):
            self.locations[wordsDict[i]].append(i)
        
    
    def shortest(self, word1, word2):
        shortest = float("inf")
        list1 = self.locations[word1]
        list2 = self.locations[word2]

        l1 = l2 = 0

        while l1 < len(list1) and l2 < len(list2):
            shortest = min(shortest, abs(l1 - l2))
            if list1[l1] < list2[l2]:
                l1 += 1
            else:
                l2 += 1
            
        return shortest