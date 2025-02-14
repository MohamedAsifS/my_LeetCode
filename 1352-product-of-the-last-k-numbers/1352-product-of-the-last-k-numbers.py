class ProductOfNumbers:

    def __init__(self):
        self.stack=[]
        self.zero=-1
        self.res=1
        

    def add(self, num: int) -> None:
        if num==0:
            self.zero=len(self.stack)
            self.res=1
            self.stack.append(0)
        else:
            self.res*=num
            self.stack.append(self.res)
        # print(self.stack)
     
        
        

        

    def getProduct(self, k: int) -> int:
        length=len(self.stack)
        if length-k <= self.zero:
            return 0
        elif  length-k == (self.zero+1):
            return self.stack[-1]
        print(self.stack[-1],self.stack[(length-1)-k],k,self.zero,self.stack)
        
        return  self.stack[-1]//self.stack[(length-1)-k]
        
        
         

        

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)