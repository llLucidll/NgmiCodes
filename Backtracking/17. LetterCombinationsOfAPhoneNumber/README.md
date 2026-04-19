### Approach 



1. We first write out our hashmap for each digit corresponding to the letters
2. Then we iterate through the phone number given to us.
3. For each phone number, we make a DFS call with every possible letter it could be
4. We append to our results once we have hit the end of the phone number.
5. We don't need to be worried about duplicates because we are iterating forward in the phone number.





Time: O(4^N)   We generate at worst case 4 new DFS calls at each node.



Space: O(N * 4^N)   At worst case, we have 4^N cases for the N digits in the phone number.


 
