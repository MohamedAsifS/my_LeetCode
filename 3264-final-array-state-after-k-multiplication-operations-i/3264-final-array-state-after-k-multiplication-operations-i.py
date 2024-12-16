
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        count=[]
        for i,v in enumerate(nums):
            temp=[v,i]
            count.append(temp)
        
      
        heapq.heapify(count)
        
        

        for i in range(k):
            num=heapq.heappop(count)
            num[0]=num[0]*multiplier
            heapq.heappush(count,num)
        
        for i in count:
            nums[i[1]]=i[0]

        return nums
        