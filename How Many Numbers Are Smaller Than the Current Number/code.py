class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hash={}
        temp=sorted(nums)
        for i in range(len(temp)):
            if temp[i] not in hash:
                hash[temp[i]]=i
        res=[]
        for i in nums:
            res.append(hash[i])
        return res

        
                

        