
class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(opening, closing, sub):
            if opening == closing == n:
                res.append(sub)
                return 
            
            if opening > closing:
                dfs(opening, closing + 1, sub + ")")
            if opening < n:
                dfs(opening + 1, closing, sub + "(")

        dfs(0, 0, "")
        return res

