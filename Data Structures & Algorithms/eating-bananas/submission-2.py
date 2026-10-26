class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        nuMax = max(piles)
        l = 1
        r = nuMax
 
        res = nuMax


        while(l <= r):
            mid = (l + r )//2
            hourMid = 0;
            for i in range(len(piles)):
                hourMid += math.ceil(piles[i] / mid )
            if(hourMid > h):
                l = mid + 1
            elif(hourMid <= h):
                res = mid
                r = mid - 1
            




        return res
            
        