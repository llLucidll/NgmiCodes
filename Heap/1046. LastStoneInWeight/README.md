**Approach**



1. Initalize a maxHeap and keep popping from it as long as the length is >=2 
2. If the two stones are unequal we push the difference to the heap 
3. Once we have only one stone left we return it. If there are no stones left then we return 0




Time: O(nlogn) where n is the number of stones 




Space: O(n) stores all n stones in the heap