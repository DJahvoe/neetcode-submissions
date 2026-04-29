class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # convert into max-heap
        self._data = [-num for num in nums]
        heapq.heapify(self._data)

    def add(self, val: int) -> int:
        # inserting into max-heap
        heapq.heappush(self._data, -val)
        return -heapq.nsmallest(self.k, self._data)[self.k - 1]
        
