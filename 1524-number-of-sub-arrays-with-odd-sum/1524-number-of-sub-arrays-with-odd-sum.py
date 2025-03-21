class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum=0
        even=0
        odd=0
        res=0

        for n in arr:
            cur_sum+=n
            if cur_sum % 2 :
                res+=1 + even
                odd+=1
            else:
                res+=odd
                even+=1
        return res % (10**9+7)
        