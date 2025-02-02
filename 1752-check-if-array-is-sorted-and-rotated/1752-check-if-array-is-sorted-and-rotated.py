class Solution:
    def check(self, nums: List[int]) -> bool:

        check=sorted(nums)


        for i in range(len(nums)):
            n=nums.pop(0)
            nums.append(n)
            if check==nums:
                return True
        return False

        