class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
         
      


        


        res=[]
        check=set()

        for  i in range(1,len(groups)):
            if groups[i-1]==groups[i]:
                  check.add(i)

        for i in range(len(groups)):
            if i not in check:
                res.append(words[i])
        return res
       
                
       
           
        
        