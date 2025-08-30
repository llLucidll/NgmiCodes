**Approach**




1. First we initalize two count arrays for both the strings which are the length of the English alphabet.
2. Then we count the length of s1 in both s1 and s2 and update the count arrays
3. We check for the matches and if all the indices of the Count arrays match (26) then we return True
4. Otherwise, we move our sliding window which is the length of string s1 until we either parse through all of s2 or we find a match matches == 26



Time: O(n)   Where n is the length of the longer string



Space: O(26 * 2) = O(1)   Since we have two arrays of length 26