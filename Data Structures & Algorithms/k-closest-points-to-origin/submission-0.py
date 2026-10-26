class Solution:
   
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = {}
        heap = []
        for arr in points:
            a =  math.pow(arr[0], 2) + math.pow(arr[1], 2)
            heapq.heappush(heap, (a, (arr)))

        resArr = []

        for i in range (k):
            tmp = heapq.heappop(heap)
            distance, point = tmp

            resArr.append(point)

        return resArr
        


        

