class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        hash={}

        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        check=len(nums)//2
        need=len(nums)//check
        if need%2!=0:
            return False



        for i in hash:
            if hash[i]%need!=0:
                return False
        return True

            
            

        