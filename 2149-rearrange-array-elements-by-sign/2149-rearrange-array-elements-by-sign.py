class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        res=[]

        num1=[]
        num2=[]

        for i in nums:
            if i >=0:
                num1.append(i)
            else:
                num2.append(i)
        for i in range(len(num1)):
            res.append(num1[i])
            res.append(num2[i])
        return res