class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        m2 = {}

        for c in s:
            m[c] = m.get(c, 0) + 1
        
        for c in t:
            m2[c] = m2.get(c, 0) +1 
        
        if m == m2:
            return True

        return False