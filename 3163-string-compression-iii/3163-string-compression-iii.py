class Solution:
    def compressedString(self, word: str) -> str:
        if len(word)==1:
            return "1"+word
        temp=1
        comp=""
        v=[]
        for i in word:
            v.append(i)
        for i in range(1,len(v)):
            if v[i]==v[i-1]:
                temp+=1
           

            elif v[i-1] !=v[i] :
                print(temp)
                while temp>=9:
                   
                    comp+=str(9)
                    comp+=v[i-1]
                    temp-=9
                if temp >0:
                    print(temp)
                    comp+=str(temp)
                    comp+=v[i-1]
                    temp=1
                if temp==0:
                    temp=1
                
                
           
            prev=v[i]
       
        if temp >9:
            while temp>=9:
                   
                    comp+=str(9)
                    comp+=v[i-1]
                    temp-=9
                    if temp >0:
                       comp+=str(temp)
                       comp+=v[i-1]
                       temp=1
            return comp
        if temp==0:
            temp=1
        
        
        return comp+str(temp)+v[i]






       