**Approach**


1. We initialize a dictionary words to remember how many words are there in the same anagram class
2. We go through the list and at each word, we sort it and if its already a key in the dictionary we append it, otherwise we set a new key with that word as the value
3. At the end we use the list(word.values()) to return a list of lists where each key's values are embedded lists.


Time: O(n) 1 for loop 


Space: O(n) We are storing the words in our dictionary 