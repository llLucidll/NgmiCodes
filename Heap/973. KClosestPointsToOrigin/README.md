**Approach**


1. Heap Solution

1. First we take every coordinate in our input and add it to our array minHeap along with the information about the distance from origin as the first element in the list. So [distance, [coord]] is appended to the array

2. Then we heapify the array so that the heap arranges the elements based on the distance.
3. Since we have a minHeap, until k is 0 we pop the top of the heap to get the k closest points to origin!
4. Append those to an array and return them



Time: NlogK (N elements in the heap, k deletions from the heap)


Space: O(n) since we insert the entire n elements into memory first.