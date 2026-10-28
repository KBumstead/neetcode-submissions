class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for n in nums:
            for i in range(len(subs)):
                subs.append(subs[i] + [n])

        return subs

