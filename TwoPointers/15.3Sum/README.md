**Approach**


1. We need to find a list of all triplets in the input array such that they sum to 0
2. First we start by having a for loop.
    1. Within the for loop we set two pointers on opposite ends of the subarray
    2. If the current sum is greater than 0 we move right pointer to left
    3. If its less than 0 we move the left pointer to the right.
    4. If we find it sums to 0 then we add it to our result.
3. We need to make sure we dont add duplicate triplets. So we have to add logic into each loop which says if list[i] == list[i-1] when i > 0, then we continue
Similarly if list[j] = list[j-1] when j > 0 then we keep incrementing j by 1



Time: O(n) we parse through the entire nums list


Space: O(1) We are not storing anything.