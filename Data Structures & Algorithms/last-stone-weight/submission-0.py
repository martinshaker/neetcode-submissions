class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        print(maxHeap)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if y > x:
                heapq.heappush(maxHeap, x - y)

        if maxHeap:
            print(maxHeap[0])
            return maxHeap[0]*-1
        else:
            return 0



        