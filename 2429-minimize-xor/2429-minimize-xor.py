class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bit_c=0
        
        while(num2):
            num2=num2 & num2-1
            set_bit_c +=1
        res=[]
      
        x=num1
        num1=bin(num1)[2:]
        print(num1,set_bit_c)

        for i in range(len(num1)):
            if set_bit_c >= 1 and  num1[i]=="1":
                res.append("1")
                set_bit_c-=1
            else:
                res.append("0")
        count=len(num1)-1
        print(count)
        while set_bit_c >=1 :
            print(count,set_bit_c )
            if count == 0 and set_bit_c >= 1:
                print(count,set_bit_c,"a")
                res.append("1")
                set_bit_c-=1
            elif res[count]  == "0" and set_bit_c >= 1:
                   res[count]="1"
                   set_bit_c-=1
            else:
                count-=1
        res="".join(res)
        print(res)
        
        
                
            
        return int(res,2)
         


        
       
