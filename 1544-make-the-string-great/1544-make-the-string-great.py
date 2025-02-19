class Solution:
    def makeGood(self, s: str) -> str:

        stack=[]
      

        for i in s:
           if stack and stack[-1]!=i: 
               if stack and stack[-1]==i.upper() or stack and stack[-1]==i.lower() :
                       stack.pop()
               else:
                stack.append(i)
           else:
                stack.append(i)
        return "".join(stack)
            
        