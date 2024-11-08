class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxi = -1
        num = nums[0]
        res = []
        res.append(nums[0])

        for i in range(1, len(nums)):
            num = num ^ nums[i]
            res.append(num)
        mask = (2**maximumBit) - 1

        for i in range(len(res)):
            res[i] = res[i] ^ mask
        res.reverse()

        return res

        return res
