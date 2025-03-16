class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1=nums[:n]
        num2=nums[n:]
        res=[]
        for i in range(n):
             res.append(num1[i])
             res.append(num2[i])
        return res

