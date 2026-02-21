### Approach 


First we count occurences of all strings and then within the index bounds, we measure the distance to decide which one to append to our results array


Time: O(m * n) because when we are counting occurences, we are checking m characters and we do that n times (at each index)



Space: O(n) results array basically


Extra notes: We could optimize this time complexity to O(n) if we used Z algorithm / KMP algorithm.