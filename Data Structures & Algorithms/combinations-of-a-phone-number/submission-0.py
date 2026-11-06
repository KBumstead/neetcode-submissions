class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {}
        maps["2"] = ["a", "b", "c"]
        maps["3"] = ["d", "e", "f"]
        maps["4"] = ["g", "h", "i"]
        maps["5"] = ["j", "k", "l"]
        maps["6"] = ["m", "n", "o"]
        maps["7"] = ["p", "q", "r", "s"]
        maps["8"] = ["t", "u", "v"]
        maps["9"] = ["w", "x", "y", "z"]

        if digits == "":
            return []

        res = []
        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            if i > len(digits):
                return
            
            nums = maps[digits[i]]
            for num in nums:
                curr += num
                backtrack(i + 1, curr)
                curr = curr[:-1]
        
        backtrack(0, "")

        return res