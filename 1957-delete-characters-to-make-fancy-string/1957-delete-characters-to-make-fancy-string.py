class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""
        count=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            elif s[i-1]!=s[i]:
                count=0
            if count <2:
                res+=s[i-1]
        return res+s[len(s)-1]


        