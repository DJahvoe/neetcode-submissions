class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)
        
        while len(stone_heap) > 1:
            first_stone = heapq.heappop(stone_heap)
            second_stone = heapq.heappop(stone_heap)
            heapq.heappush(stone_heap, -abs(first_stone - second_stone))
        
        return -stone_heap[0]
