class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
      
    

        ans={}
        count=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                cal=nums[i]*nums[j]
                if cal not in ans:
                    ans[cal]=1
                else:
                    ans[cal]+=1
        print(ans)
        for i in ans:
             p=((ans[i]-1)*ans[i]//2)
             count+=p*8
            
            

                
           
    
        return count
                
                
        