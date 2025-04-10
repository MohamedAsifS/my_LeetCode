class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        path=set()
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                path.add(i)
        return len(path)

        
        