class Solution:
    def hammingWeight(self, n: int) -> int:

        s=bin(n)[2:]

        res=0

        for i in s:
            if i=="1":
                res+=1
        return res
        