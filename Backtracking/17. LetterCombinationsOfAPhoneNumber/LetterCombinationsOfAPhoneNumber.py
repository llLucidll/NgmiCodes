class Solution:
    def letterCombinations(self, digits: str):
        res = []
        digit_map = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 
        4: ["g", "h", "i"], 5: ["j", "k", "l"], 
        6: ["m", "n", "o"], 7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}


        def dfs(current, result):
            if current == len(digits):
                res.append(result)
                return 

            number = int(digits[current])
            letters = digit_map[number]

            for letter in letters:
                dfs(current + 1, result + letter)

        dfs(0, "")
        return res if len(digits) != 0 else []


