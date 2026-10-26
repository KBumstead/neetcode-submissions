class Solution {
    public int[] productExceptSelf(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < nums.length; i ++){
            int temp = 1;
            for(int j = 0; j < nums.length; j++){
                if(j == i){
                    continue;
                }  
                else{
                    temp *= nums[j];
                }
            }
            res.add(temp);
        }   
        int[] resultArray = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            resultArray[i] = res.get(i);
        }
        return resultArray;
    }
}  
