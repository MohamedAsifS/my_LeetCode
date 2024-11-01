class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[0]
        temp_count=1
    

        for i in range(1,len(s)):
            if s[i]==res[-1]:
                temp_count+=1

                if temp_count<3:
                    res+=s[i]
            else:
                temp_count=1
                res+=s[i]
        return res

            

        
            

        