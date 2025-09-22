**Approach**

1. Heap Solution
    1. First we take the first k elements of the list and heapify it into our minheap
    2. We maintain the size of our heap as k, so we pop the top of the heap and append a new element from the rest of the list if it is greater than minHeap[0]
    3. We return the top of the ksized heap at the end as the kth largest element 


Time: O(nlogk)


Space: O(k)  As we store the max k elements.



2. TODO: Quick Select Solution





