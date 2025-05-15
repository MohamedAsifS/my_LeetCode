class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        val1=[0]*26
        val2=[0]*26

        for i in s:
            val1[ord(i)-97]+=1
        for j in t:
            val2[ord(j)-97]+=1
       
        
        return val1==val2
            
        