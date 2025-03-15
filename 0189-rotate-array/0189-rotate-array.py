class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        to=k%n
        if to==n:
            return nums
        while to>0:
            val=nums.pop()
            nums.insert(0,val)
            to-=1
        


        