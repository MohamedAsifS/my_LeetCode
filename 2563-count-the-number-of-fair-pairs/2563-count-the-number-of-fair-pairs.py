class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def Bianry_search(l,r,target):
            while l<=r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1
            return r

        #O(logn)

    

        nums=sorted(nums)

        count=0

        for i in range(len(nums)):
            low=lower-nums[i]
            up=upper-nums[i]

            count+=(Bianry_search(i+1,len(nums)-1,up+1)-
            Bianry_search(i+1,len(nums)-1,low))

                     
             
              
           
        return count

        
        