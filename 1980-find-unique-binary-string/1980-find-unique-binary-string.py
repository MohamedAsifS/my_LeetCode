from itertools import permutations
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr=['0','1']*len(nums[0])
        check=set()
        for i in nums:
            temp=list()
            for j in i:
                temp.append(j)
            check.add(tuple(temp))
        


 
        
        for i in permutations(arr,len(nums[0])):
           if i not in check:
            return "".join(i)
        
        