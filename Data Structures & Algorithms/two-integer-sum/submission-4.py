class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i,val in enumerate(nums):
            num = target - val
            if num in map:
                return [map[num], i]
            map[val] = i
            