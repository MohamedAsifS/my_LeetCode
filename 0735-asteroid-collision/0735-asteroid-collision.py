class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]

        for i in asteroids:
            while res and i < 0 <res[-1]:
                if -i > res[-1]:
                    res.pop()
                    continue
                elif -i == res[-1]:
                    res.pop()
                break
            else:
                res.append(i)
        return res
            
            



                     





            
        