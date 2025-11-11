**Approach**

My solution cycles through two processes.
Process 1: Adds all the current rotten oranges to the rotten queue for processing. We process the entire queue and add all adjacent neighbours to the fresh_q


Process 2: If the fresh_q is not empty after processing the rotten_q, we convert all those fresh oranges to rotten oranges and then add those to the rotten q.

Things to keep in mind:
1. we increment time everytime we finish processing the rotten q completely.
2. before we start processing either queue, when we go through the entire grid for adding the first rotten oranges, also count the number of fresh oranges. If they are 0 then we must catch this edge case and instantly return 0 as the count.


Time: O(n*m) Where the grid has n rows and m columns



Space: O(n*m) due to the worst case scenario where every node of the grid could end up in a queue.