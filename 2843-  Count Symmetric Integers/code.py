class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
               s=str(i)
               if len(s)%2==0:
                    mid=len(s)//2
                    if sum(int (i) for i in s[:mid]) == sum(int(i) for i in s[mid:]):
                        count+=1
      
        return count
        