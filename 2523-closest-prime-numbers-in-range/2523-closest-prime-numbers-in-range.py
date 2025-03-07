class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # we use here algorithim is seive for more optimal way

        if right < 2:
            return [-1,-1]

        prime = [True]*(right+1)
        prime[0]=False
        prime[1]=False

        for i in range(2,int(right**0.5)+1):
            if prime[i]==True:
                for j in range(i*i,right+1,i):
                    prime[j]=False
        num=[]
        count=left
        for i in prime[left:right+1]:
            if i==True:
                num.append(count)
            count+=1
        if len(num)<2:
            return [-1,-1]
        
        final=[0]*2
        res=float('inf')
  
        for i in range(1,len(num)):
            if num[i]-num[i-1]<res:
                
                res=num[i]-num[i-1]
       
                final[0]=num[i-1]
                final[1]=num[i]
        return final
        
            

      
      
      