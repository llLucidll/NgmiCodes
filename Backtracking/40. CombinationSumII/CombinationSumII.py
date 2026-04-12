class Solution:
    def combinationSum2(self, candidates, target: int):
        result = []
        candidates.sort()

        def dfs(i, total, subset):
            if total > target:
                return 
            if total == target:
                result.append(subset.copy())
                return 
            
            while i < len(candidates):
                subset.append(candidates[i])
                dfs(i + 1, total + candidates[i], subset)
                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    i += 1
                subset.pop()
                i += 1
        
        dfs(0, 0, [])
        return result
            

        