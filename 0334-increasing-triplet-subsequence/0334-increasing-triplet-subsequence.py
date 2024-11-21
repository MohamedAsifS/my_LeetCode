class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
                print(nums[i],nums[i-1],count)
           
        print(count)
        if count>=3:
            return True
        else:
            return False
