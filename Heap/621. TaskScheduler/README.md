**Approach**


### Max heap Solution 
1. First we tally up the frequencies of each task and then we take all those counts and put them into our maxHeap
2. then we initialize a queue to hold the tasks while they are still on cooldown (The n constraint)
3. if the heap is empty, we can just skip ahead to the time of the first task in the queue (idle)
4. at each instance of the loop we increment the time += 1 and we also check if the time == to the task at the front of the queue.


Time: O(m) where m is the number of tasks assigned to us.

Space: O(1) 