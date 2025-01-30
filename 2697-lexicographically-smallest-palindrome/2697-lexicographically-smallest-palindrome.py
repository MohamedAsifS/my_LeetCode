class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        res=[]

        for i in s:
            res.append(i)

        r=0
        l=len(s)-1

        while r <= l:
            if res[r] != res[l]:
                if res[r] < res[l]:
                    res[l]=res[r]
                else:
                    res[r]=res[l]
            r+=1
            l-=1
        return "".join(res)
        