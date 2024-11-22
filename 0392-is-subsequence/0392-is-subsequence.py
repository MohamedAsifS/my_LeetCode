class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0 :
            return True
        elif len(t)==0:
            return False
        l1=0
        l2=0
        while l2!=len(t) and l1!=len(s):
            if s[l1]==t[l2]:
                l1+=1
            l2+=1
        if l1< len(s):
            return False
        return True
        
        