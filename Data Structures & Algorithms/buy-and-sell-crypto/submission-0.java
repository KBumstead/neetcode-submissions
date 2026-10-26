class Solution {
    public int maxProfit(int[] prices) {
        int least = prices[0];
        int res = 0;
        for(int i = 0; i < prices.length; i++){
          
            if(least > prices[i]){
                least = prices[i];
            }
            if(least < prices[i]){
                int temp = prices[i] - least;
                if(temp > res){
                    res = temp;
                }
            }
        }

        return res;
    }
}
