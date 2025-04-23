class Solution:
    def sumN(self,n):
        val=0
        while n>>0:
            digit=n%10
            val+=digit
            n//=10
        return val
    def countLargestGroup(self, n: int) -> int:

        mapi={}
        gre=0

        for i in range(1,n+1):
            cal=self.sumN(i)
            if cal not in mapi:
                mapi[cal]=1
            else:
                mapi[cal]+=1
            gre=max(gre,mapi[cal])
        count=0
    
        for i in mapi:
            if mapi[i]==gre:
                count+=1
        return count

            


        