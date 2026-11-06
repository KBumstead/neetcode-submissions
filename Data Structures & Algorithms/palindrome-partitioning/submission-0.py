class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            i = 0
            j = len(word) - 1

            while i < j:
                if word[i] != word[j]:
                    return False

                i += 1
                j -= 1
                
            return True

        

        res = []


        def backtrack(i, curr):
            if i >= len(s):
                res.append(curr.copy())
                return
            

            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    curr.append(s[i :  j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()


        backtrack(0, [])

        return res
                