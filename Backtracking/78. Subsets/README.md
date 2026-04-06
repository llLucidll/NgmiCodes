### Approach 



1. As we go through the list of numbers, for each number our method does two calls -> one adding that element in and one deciding not to add that element in 

2. So if our list was just [1], our first call would be 
    1. Add 1 in -> [1]
    2. Don't add 1 in -> []


3. Let's do this with a larger example, [1, 2]
    1. Add 1 in -> [1] (1)
    2. Don't add 1 in -> [] (2)

    (1) -> Add 2 in [1, 2] (3), appends to result [1, 2]
    (1) -> Don't add 2 in [1] (4) appends to result [1]

    (2) -> Add 2 in [2] (5), appends to result [2]
    (2) -> Don't add 2 in [] (6), appends to result [] 

    This gives us a final state of [[1, 2], [1], [2], []]




Time: O(n * 2^n) 



Space: O(n) extra space recursion stack; O(2n) for the output.
