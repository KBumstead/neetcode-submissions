class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;
        int area = 0;

        while(l < r){
            int length = r - l;
            int height = Math.min(heights[l], heights[r]);
            int currArea = length * height;
            if(currArea > area){
                area = currArea;
            }
            if(heights[l] < heights[r]){
                l+=1;
            }
            else{
                r-=1;
            }



        }
        return area;
    }
}
