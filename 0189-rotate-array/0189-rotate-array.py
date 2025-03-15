class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        to=k%len(nums)
        if to==len(nums):
            return nums
        while to>0:
            val=nums.pop()
            nums.insert(0,val)
            to-=1
        


        