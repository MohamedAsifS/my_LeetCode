class Solution:
    def reverseVowels(self, s: str) -> str:

        f={"a","e","i","o","u","A","E","I","O","U"}

        box=[]
        replace=[]

        for i in s:
             if i not in f:
                box.append(i)
             else:
                box.append(0)
                replace.append(i)
      
        res=""
        tot_len=len(replace)-1
        for i in box:
            if i!=0:
                res+=i
            else:
                res+=replace[tot_len]
                tot_len-=1
        return res




        
        

       
                 

        