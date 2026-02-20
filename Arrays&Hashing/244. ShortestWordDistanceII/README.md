### Approach


The difference in approach between 1 and 2 is that in 1, we don't want each operation to be O(N), we can reduce this time complexity by just precomputing the indices and then calculating the shortest distance only between calls.



Time : O(M + N) where M and N are the lengths of the respective index lists.



Space: O(N) For each word, we create an array of it's indices (N is number of words here.)