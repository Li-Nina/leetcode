import heapq


class Solution:
    def findKthLargest_api(self, nums: 'List[int]', k: int) -> int:
        return heapq.nlargest(k, nums)[k - 1]

    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        """
        最小堆
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


if __name__ == '__main__':
    x = Solution().findKthLargest([1, 2, 3, 4, 7, 5, 1, 0, 3], 4)
    print(x)
