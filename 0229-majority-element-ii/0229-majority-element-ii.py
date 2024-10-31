class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        const={}
        res=[]

        for i in nums:
            if i not in const:
                const[i]=1
            else:
                const[i]+=1
        cr=len(nums)//3
        for i in const:
            if const[i]>cr:
                res.append(i)
        return res


        