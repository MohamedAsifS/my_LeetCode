class Solution:
    def replaceDigits(self, s: str) -> str:
        sta=[]
        res=""
        for i in s:
            if not sta :
                sta.append(i)
                res+=i
            else:
                temp=ord(sta.pop())+int(i)
             
                res+=chr(temp)
        return res

        