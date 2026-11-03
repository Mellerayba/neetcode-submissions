import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)
        splice = len(nums)-k
        if splice>0:
            self.heap = self.heap[splice:]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
       
        return self.heap[0]
