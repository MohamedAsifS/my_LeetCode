class Solution:
    def count_1(num):
        count=0
        while num > 0:
            if num%2==0:
                pass
            else:
                count+=1
            num//=2
        return count


    def canSortArray(self, nums: List[int]) -> bool:
        print(Solution.count_1(4))
       
        

        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
               if nums[j]>nums[j+1] and Solution.count_1(nums[j]) != Solution.count_1(nums[j+1]):           
                   
                    return False
                
               elif nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return True
        