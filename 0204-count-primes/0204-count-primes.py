class Solution:
    def countPrimes(self, n: int) -> int:
        # res=0
        # for i in range(2,n):
        #     check=True
        #     for j in range(2,(i//2)+1):
        #           if i%j==0:
        #             check=False
        #             break
        #     if check:
        #         print(i)
        #         res+=1
        # return res
        

        # above code is not optimal but we can use Sieve of Eratosthenes approach

        if n <=2:
            return 0

        prime=[True]*(n)
        prime[0],prime[1]=False,False

        

       
        
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=False
                    
        count=0
        for i in prime:
            if i==True:
                count+=1
                
      
        return count
         
        