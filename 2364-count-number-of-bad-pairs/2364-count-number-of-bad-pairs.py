class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        good_pairs=0

        total_pairs=0

        count=defaultdict(int)

        for i in range(len(nums)):
               total_pairs+=i
               num=nums[i]-i
               good_pairs+=count[num]
               count[num]+=1
        return total_pairs-good_pairs

        