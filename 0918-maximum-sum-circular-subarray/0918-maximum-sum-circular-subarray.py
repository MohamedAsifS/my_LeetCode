class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadens alogrithim plus here we need to find the two edge case one is highest in midle and in cirular
        #with previous we know how to find the middle (by lsoing minus we will get)
        # for circular we need to find total_sum - least subarray (its a whole wrapped)

        globalMax,globalmin=nums[0],nums[0]
        cur_min,cur_max=0,0
        total_sum=0
        for i in nums:
            cur_max=max(cur_max+i,i)
            cur_min=min(cur_min+i,i)

            total_sum+=i
            globalMax=max(globalMax,cur_max)
            globalmin=min(globalmin,cur_min)
        return globalMax if globalMax <0 else max(globalMax,total_sum-globalmin) 



        

           
        
        