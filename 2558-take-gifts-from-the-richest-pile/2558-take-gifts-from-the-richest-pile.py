import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            last = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(last)))
        return -sum(gifts)
