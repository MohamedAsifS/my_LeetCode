class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        ans=""

        min_select_len=0
        long_select=0
        large=""

        if len(word1)==len(word2):
            min_select_len=len(word1)
            long_select=len(word1)

        elif len(word1)>len(word2):
            
            min_select_len=len(word2)
            large=word1
        else:
            
            min_select_len=len(word1)
            large=word2
        

        for i in range(min_select_len):
            ans+=word1[i]
            ans+=word2[i]
        
        if min_select_len==long_select:
            return ans
        else:
            ans+=large[min_select_len:]
            return ans


        
        
        