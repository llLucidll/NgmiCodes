**Approach**



1. We will be discussing the heap solution which I found was the most intuitive to me.
2. For heaps to work, we need a new class NodeWrapper with a built in method __lt__ which is a comparision so the heap can figure out which element is lower in value 
3. Then we will start by inserting each list head into our minHeap
4. Then we declare a result node and a cursor
5. While the minHeap is non empty, we continue to pop elements in the order the minHeap gives it to us. If the node we popped is not the end of that list, we also add that element into the heap whcih automatically sorts it.
6 At the end we return the res.next 




Time: O(nlogk) Because for all the n elements we insert/drop into the heap, we have to pay a logk price




Space: O(k) we will store k elements at the end in our newly formed merged list where k is the sun of all elements
