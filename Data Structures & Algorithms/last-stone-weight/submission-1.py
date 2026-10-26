class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)

            c = abs(a-b)

            if c > 0 :
                stones.append(c)

        if len(stones) == 0:
            return 0

        return stones[0]