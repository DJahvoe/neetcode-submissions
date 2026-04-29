class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # convert into max-heap
        self._data = nums
        heapq.heapify(self._data)
        while len(self._data) > k:
            heapq.heappop(self._data)

        print(self._data)

    def add(self, val: int) -> int:
        # inserting into min-heap
        heapq.heappush(self._data, val)
        if len(self._data) > self.k:
            heapq.heappop(self._data)
        print(self._data)
        return self._data[0]
        
