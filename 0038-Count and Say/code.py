class Solution:
    def cal(self,val):
        res=""
        count=1
        for i in range(1,len(val)):
            if val[i-1]==val[i]:
                count+=1
            else:
                res+=str(count)+val[i-1]
                count=1
        res+=str(count)+val[-1]
        return res



    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        cur="11"
        for i in range(2,n):
            cur=self.cal(cur)
       
        return cur



        