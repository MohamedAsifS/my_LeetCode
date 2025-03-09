class Solution:
    # def check(self,colors,starting,ending):
        
    #     for i in range(starting,ending):
           
    #         if colors[i]==0 and colors[i-1]!=1 or colors[i]==0 and colors[i+1]!=1:
                
    #             return False
    #         elif colors[i]==1 and colors[i-1]!=0 or colors[i]==1 and colors[i+1]!=0:
          
    #             return False
       
    #     return True
       
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # current=True
        # for i in range(1,k-1):
        #       if colors[i]==0 and colors[i-1]!=1 or colors[i]==0 and colors[i+1]!=1:
        #         current=False
        #       elif colors[i]==1 and colors[i-1]!=0 or colors[i]==1 and colors[i+1]!=0:
        #         current=False


       
        ksize=colors[0:k-1]
        colors=colors+ksize
        # print(colors,current)
        
        l=0
        N=len
        count=0
        for r in range(1,len(colors)):
            #   print(l,r)
              if colors[r]==colors[r-1]:
                         l=r
              if (r-l)==k-1:

                  count+=1
                  l+=1
        return count



        return 0
        