import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if (
            (self.maxHeap and self.minHeap) and
            (-self.maxHeap[0] > self.minHeap[0])
        ):
            last = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -last)
        if len(self.maxHeap)> len(self.minHeap)+1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap) +1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()