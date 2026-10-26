class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # s = set()
        # for i in range (len(nums)):
        #     if nums[i] in s:
        #         return nums[i]
        #     else:
        #         s.add(nums[i])

        nums.sort()
        for i in range(len(nums)):
            if ((i + 1) < len(nums)):
                if nums[i] == nums[i + 1]:
                    return nums[i]

        return 0;