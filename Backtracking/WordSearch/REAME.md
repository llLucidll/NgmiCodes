### Approach 


1. We scour through the entire board to find the first letter in the word.
2. Once we find the first letter, we make DFS calls to all surrounding neighbours to find the next letter.
3. We use a path set to make sure we don't use the same index twice
4. If the curr index + 1 is = to the length of the word, then we know our current call has completed the word and we bubble True back up through the stack





Time: O(M * N * 3^L)    M * N is from traversing the entire grid. At every node, we can recurse up to three different directions (excluding the direction that is currently in path)




Space: O(M * N)     at worst case, our path set can contain all nodes inside of the grid 
