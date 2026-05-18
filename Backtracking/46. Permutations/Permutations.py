class Solution:
    def permute(self, nums):
        result = []

        def dfs(curr, avail):
            if not avail:
                result.append(curr)
                return 

            for i in range(len(avail)):
                curr_copy = curr.copy()
                avail_copy = avail.copy()

                curr_copy.append(avail[i])
                avail_copy.pop(i)
                dfs(curr_copy, avail_copy)

        dfs([], nums)
        return result

