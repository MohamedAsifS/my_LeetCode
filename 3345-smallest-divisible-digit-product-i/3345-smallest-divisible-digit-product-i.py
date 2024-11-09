class Solution:
    def prod(num):
        res=1
        while num!=0:
            digit=num%10
            res*=digit
            num//=10
        return res
    def smallestNumber(self, n: int, t: int) -> int:

        for i in range(n,101):
       
                
            if Solution.prod(i)==0:
                return i
            elif Solution.prod(i)%t==0:
                return i
            