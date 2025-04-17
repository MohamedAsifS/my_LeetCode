class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hash={}
        count=0

        for i in range(len(nums)):
            if nums[i] not in hash:
                val=[]
                val.append(i)
                hash[nums[i]]=val
            else:
                for j in hash[nums[i]]:
                    if (j*i)%k ==0:
                        count+=1
                hash[nums[i]].append(i)
        return count
        