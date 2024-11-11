class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        b=0
        c=0


        sec={}

        gue={}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b+=1
            else:
               if secret[i] not in sec:
                    sec[secret[i]]=1
               else:
                     sec[secret[i]]+=1
                


               if guess[i] not in gue:
                     gue[guess[i]]=1
               else:
                     gue[guess[i]]+=1
              
                
               if secret[i] in gue and gue[secret[i]]>0:
                     c+=1
                     gue[secret[i]]-=1
                     sec[secret[i]]-=1
               if guess[i] in sec and sec[guess[i]]>0:
                      c+=1
                     
                      sec[guess[i]]-=1
                      gue[guess[i]]-=1
              
        return str(b)+"A"+str(c)+"B"
                    
                   