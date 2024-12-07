class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned_set=set(banned)

        ts=0
        c=0

        for i in range(1,n+1):
            if i in banned_set:
                continue
            ts+=i
            if ts>maxSum:
                break
            c+=1
        return c