class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        count=0
        dif=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                dif.append(i)
        
        if count!=2 :
            return False
        
        return s1[dif[0]]==s2[dif[1]] and s1[dif[1]]==s2[dif[0]]
        
       
            
        