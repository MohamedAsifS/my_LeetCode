class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count={}
        res=[]

        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i in count:
            if count[i]>1:
                res.append(i)
        return res
        