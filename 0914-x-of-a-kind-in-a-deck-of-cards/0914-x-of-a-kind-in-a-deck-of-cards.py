class Solution:
    # def isprime(self,num):
    #     for i in range(2,num):
    #         print(num,i,num%i)
    #         if num%i==0:
           
    #             return False
    #     return True

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<=1:
            return False
    
    
        

        const={}

        for i in deck:
            if i not in const:
                const[i]=1
            else:
                const[i]+=1
       
        box=list(const.values())

        if gcd(*box)>1:
            return True
        return False