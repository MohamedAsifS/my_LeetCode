class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count=0
        res=0

        for i in arr:
            if i%2==1:
                count+=1
                res=max(res,count)
            else:
                count=0
        if res >=3:
            return True
        else:
            return False