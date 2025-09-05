**Approach**




1. We maintain a heap of size k and discard all elements that are less than the kth largest.
2. This way we dont lose any information as those elements can never make it into the top k
3. We return the top of the minHeap of sizek every time we add a number which is always the kth largest element in the stream




Time: O(m * logk) where m is number of times add() is used



Space: O(k) We only store the top k elements at any instance 