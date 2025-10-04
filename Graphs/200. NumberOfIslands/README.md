**Approach**



1. DFS (Recursive)
    1. We design our DFS function to iteratively check each node above, below, left and right of it.
    2. It marks any nodes that are 1 as "0" to count it as visited.
    3. We count the island for all the connected 1's and then we try to find the next disjoint 1 and do the process again

Time complexity: O(N * M) where N is the number of rows and M is the number of columns -> The for loop parses through all rows and columns



Space: O(N*M) Worst case recursion stack size (All  nodes are "1" and connected)


2. BFS:
    1. We maintain a queue of elements at the current bfs node and we set our current node to "0"
    2. Then we set all the child nodes to "0" assuming they are "1" (Otherwise they are not added to the queue) This saves us some overhead
    3. We count an island every time BFS is called independently from the main loop


Time: O(N*M) where N is the number of rows and M is the number of columns


Space: O(N*M) Worst case queue size