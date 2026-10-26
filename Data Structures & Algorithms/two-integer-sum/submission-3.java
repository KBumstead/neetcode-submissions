class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++){
            int num = target - nums[i];
            if(!map.containsKey(num)){
                map.put(nums[i], i);
            }
            else{
                return new int[]{map.get(num), i};
            }
        }

        return new int[]{0, 0};

    }}

