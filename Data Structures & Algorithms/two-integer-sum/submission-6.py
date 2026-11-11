class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in m:
                return [m.get(res), i]
            else:
                m[nums[i]] = i

        return [0,0]
