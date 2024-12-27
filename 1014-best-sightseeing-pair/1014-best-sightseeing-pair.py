class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        res=0
        maxi=values[0]
        indi=0
        for i in range(1,len(values)):
               
                print(res,maxi,indi,i)
                res=max(res,maxi+values[i]+(indi-i))
                
                if maxi-i < values[i]-indi:
                    maxi=values[i]
                    indi=i
               
                  
                
               
        return res

