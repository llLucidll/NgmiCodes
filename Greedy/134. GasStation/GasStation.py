class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        index = 0
        max_sum = 0
        curr_sum = 0

        for i in range(len(gas)):
            curr_sum += gas[i] - cost[i]
            max_sum += gas[i] - cost[i] 

            if curr_sum < 0:
                curr_sum = 0
                index = i + 1

        return -1 if max_sum < 0 else index
