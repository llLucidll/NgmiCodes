**Approach**

I. HashMap Solution
1. Initialize two hashmaps for both strings.
2. Go through both strings and remember the frequency of the letters using the hashmap
3. Return if hashmap1 == hashmap2

Time: O(n+m) n = length of array, m = length of dictionary
Space: O(1) There are maximum of 26 possible alphabets in each hashmap.
