class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        box=set()
    

        for i in arr:
            temp=i*2
            div=i/2
            if temp in box or div in box:
                   return True
            else:
                box.add(i)
            
           
   
        return False

        