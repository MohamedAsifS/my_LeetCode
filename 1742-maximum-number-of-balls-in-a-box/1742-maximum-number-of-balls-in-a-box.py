class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        num={}

        for i in range(lowLimit,highLimit+1):
            sum=0
            while i>0:
                digit=i%10
                sum+=digit
                i//=10
            if sum not in num:
                num[sum]=1
            else:
                num[sum]+=1
            
        value=list(num.values())
        maxi=max(value)
       
        
        return maxi