class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #O(n^3)
        # res=0

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             res=max(res,(nums[i]-nums[j])*nums[k])
        # return res


        #O(n^2)

        left=nums[0]
        res=0
        for j in range(1,len(nums)):
            if nums[j]>left:
                left=nums[j]
            for k in range(j+1,len(nums)):
                        res=max(res,(left-nums[j])*nums[k])
        return res


       
        


        
        