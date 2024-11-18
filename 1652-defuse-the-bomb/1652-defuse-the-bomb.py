class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        length=len(code)

        
        res=[]
        if k>=0:
           code = code + code
           for i in range(len(code)):
              res.append(sum(code[i+1:k+1]))
              k=k+1
           return res[0:length]
        else:
            k=k*-1
            code =code[::-1][0:k][::-1]+code
            print(code)
            

            for i in range(len(code)):
                res.append(sum(code[i:k]))
                k=k+1
            return  res[0:length]
               
                
            
        




        


        