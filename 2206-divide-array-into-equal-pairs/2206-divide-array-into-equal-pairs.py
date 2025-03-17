class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash={}

        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in hash:
            if hash[i]%2!=0:
                return False
        return True