**Approach**



1. DFS (Recursive)
    1. We design our DFS function to iteratively check each node above, below, left and right of it.
    2. It marks any nodes that are 1 as "0" to count it as visited.
    3. We count the island for all the connected 1's and then we try to find the next disjoint 1 and do the process again

Time complexity: O(N * M) where N is the number of rows and M is the number of columns -> The for loop parses through all rows and columns



Space: O(1) We don't store anything extra into memory and as such the space is constant