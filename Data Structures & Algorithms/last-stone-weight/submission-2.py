import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)
        if len(stones) == 1:
            return abs(stones[0])
        elif not stones:
            return 0
        else:
            while len(stones) > 1:             
                heaviest = heapq.heappop(stones)
                second = heapq.heappop(stones)                
                heapq.heappush(stones,heaviest-second)

                print(stones)

        return abs(stones[0])