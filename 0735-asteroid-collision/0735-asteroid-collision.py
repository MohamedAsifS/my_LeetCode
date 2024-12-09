class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res=[]
        for i in asteroids:
            if res:
                if res[-1] == abs(i):
                    res.pop()
                elif res[-1] >= 0 and i<0 and res:
                   
                    while res[-1] >= 0 and i<0 and abs(i)>res[-1] and res:
                        print(res)
                        res.pop()
                elif res[-1]<0 and i>=0 :
                     
                        print(res)
                       
                
                else:
                    res.append(i)
            else:
                res.append(i)
        return res
         
                
                
                

      
        return res

    
            



                     





            
        