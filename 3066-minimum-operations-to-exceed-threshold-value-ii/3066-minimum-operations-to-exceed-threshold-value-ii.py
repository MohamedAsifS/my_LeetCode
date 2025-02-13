class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        count=0
        
        while nums[0]<k:
            num1=heapq.heappop(nums)
            num2=heapq.heappop(nums)
            res=num1*2 + num2
            heapq.heappush(nums,res)
            count+=1
            

        return count

            
        