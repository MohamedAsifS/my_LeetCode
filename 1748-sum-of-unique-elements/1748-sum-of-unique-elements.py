class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        const={}

        for i in nums:
            if i not in const:
                const[i]=1
            else:
                const[i]+=1
        sum=0
        for i in const:
            if const[i]==1:
                sum+=i
        return sum

        