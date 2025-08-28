**Approach**



1. First we turn the nums list into a Set
2. Then for every number in the set we check if there was a sequence including it, if yes then we just skip it
3. Otherwise we now check how long the longest sequence from this number is and update our longest count
4. Return this longest count



Time: O(n)



Space: O(n) We duplicate the list into a numSet
