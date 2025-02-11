class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:\
       

        
        while part in s:
            s=s.replace(part,"",1)
        return s
        

        # index=0
        # temp=set(part)
        # res=""
        # stack=[]
        # print(temp)
        # for i in s:
        #     if i in temp:
        #         stack.append(i)
        #         # print(stack)
        #         if part[index]==i:
        #             index+=1
        #         else:
        #             index=0
                    
                
        #         if index == len(part):
        #             print(i,stack[-1],stack)
        #             while index>0:
        #                 stack.pop()
        #                 index-=1
        #         if stack:
        #             lent=len(stack)-len(part)
        #             for i in range(lent):
        #                 if stack[i]==part[index]:
        #                     index+=1
        #                 else:
        #                     index=0
                        
                    
                
                        
        #     elif stack and i not in temp:
        #         print(i)
        #         while stack:
        #             res+=stack.pop(0)
        #     else:
        #         res+=i
        
        # if stack :
        #     while stack:
        #         res+=stack.pop(0)
        # return res