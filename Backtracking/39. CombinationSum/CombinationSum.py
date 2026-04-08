class Solution:
    def combinationSum(self, nums, target):
        result = []

        def dfs(i, subset, total):
            if total > target:
                return 
            elif total == target:
                result.append(subset)
                return 
            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, subset.copy(), total + nums[j])
                subset.pop()
        
        dfs(0, [], 0)
        return result