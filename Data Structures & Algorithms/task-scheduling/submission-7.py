class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = list(count.values())
        time = 0

        heapq.heapify_max(maxHeap)

        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                a = heapq.heappop_max(maxHeap) - 1
                if a > 0:
                    q.append([a, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time