class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        l=0
        let={"a","e","o","i","u"}
        res=0
        count=0
        for r in range(len(s)):
            if s[r] in let:
                count+=1
            if r==(k-1):
               
                res=max(res,count)
                
                if s[l] in let:
             
                    count-=1
                l+=1
                k+=1
        return res
