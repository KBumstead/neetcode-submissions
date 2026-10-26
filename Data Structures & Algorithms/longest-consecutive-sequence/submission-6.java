class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i ++){
            set.add(nums[i]);
        }
        int longest = 0;
        for (int i : set){
            if(!set.contains(i - 1)){
                int length = 0;
                while(set.contains(i + length)){
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
            return longest;
    }

}
