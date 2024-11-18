class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        length=len(code)

        code = code + code
        res=[]
        if k>=0:
           for i in range(len(code)):
              res.append(sum(code[i+1:k+1]))
              k=k+1
           return res[0:length]
        else:
            code =code+code
            k=k*-1
            count=0
            code.reverse()
            res.append(sum(code[count:k]))
            for i in range(len(code)):
                count+=3
                k+=3
                res.append(sum(code[count:k]))
            return  res[0:length]
               
                
            
        




        


        