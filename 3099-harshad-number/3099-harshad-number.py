class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=0
        if x==100:
            return 1
        elif x<=9:
            return x
        else:
            h=x
            res+=x%10
            x=x//10
            res+=x%10
            if h%res==0:
                return res
            else:
                return -1
        