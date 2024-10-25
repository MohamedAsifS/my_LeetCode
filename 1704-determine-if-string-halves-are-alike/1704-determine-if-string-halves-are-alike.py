class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s=s.lower()
        vowel={'a','e','i','o','u'}

        i=0
        j=len(s)-1

        count1=0
        count2=0

        while(i<j):
            if s[i] in vowel:
                count1+=1
            if s[j] in vowel:
                count2+=1
            
            i+=1
            j-=1
        if count1==count2:
            return True
        else:
            return False
        