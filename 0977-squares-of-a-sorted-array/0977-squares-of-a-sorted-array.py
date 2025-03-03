class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        less=[]
        count=0
        res=[]
        for i in range(len(nums)):
            if nums[i] < 0:
                less.append(nums[i]**2)
                count+=1
            else:
                nums[i]=nums[i]**2
                
   
        nums=nums[count:len(nums)]
    
        while len(nums)!=0 or len(less)!=0:
            if nums and less and nums[0] <=  less[-1]:
                res.append(nums.pop(0))
            elif nums and less and nums[0] >  less[-1]:
                res.append(less.pop())
            elif nums and not less:
                res.append(nums.pop(0))
            else:
                res.append(less.pop())

        return res

        