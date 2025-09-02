**Approach**



1. We need all our operations to be O(1) So we will be using a hashmap with an array combo (for returning the random element)
2. for the insert operation. We check if the value already exists in our hashmap. If not we update both the hashmap and append to the end of the array
3. In the remove operation, the idea is we do not want to remove from the array (shifts element O(n)). So we will move the last index element to the index we want to remove. So once we update both the dictionary and the array to carry out this operation, we will pop the duplicate last index and the entry from our dictionary.
4. We will return a random element in the range 0, len(array)




Time: O(1) on all methods



Space: O(2n) because we store both an array and a hashmap copy.