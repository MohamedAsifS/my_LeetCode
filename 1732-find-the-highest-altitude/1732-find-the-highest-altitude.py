class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        add=0
        res=[0]*len(gain)
        for i in range(len(gain)):
            res[i]=add
            add+=gain[i]
        res.append(add)
        return max(res)
            

        