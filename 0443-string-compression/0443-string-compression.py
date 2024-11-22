class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return len(chars)

        res=""
        count=1
        prev=str()
        for i in range(1,len(chars)):
           
            first=chars[i-1]
            if chars[i-1] ==chars[i]:
                count+=1
                prev=chars[i]
            elif count==1:
                res+=first
              
            else:
                res+=prev+str(count)
                count=1
        print(first)
        if count==1:
            res+=chars[i]
        elif count>1:
            res+=prev+str(count)
        chars.clear()
        for i in res:
            chars.append(i)

      
        return len(chars)


        