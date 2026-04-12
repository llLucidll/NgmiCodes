### Approach 


1. We keep track of how many opening and closing brackets we have in the current recursive call
2. if the number of opening brackets are less than n, then we are able to make a valid recursive call with one more opening bracket
3. If the number of closing brackets is less than number of opening brackets, then we are able to make a valid recursive call with one more closing bracket.
4. We append to the result array any call that makes it to n closing and opening brackets.



Time: (4^N/ n^(1.5)) to understand this google Catalan Numbers from combinatorics theory.


Space: O(N) the recursion stack goes up to N length at once
