class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        res = []
        count=k

        for i in range(len(nums)):
            temp = nums[i:k]
            indi = True
           

            if len(temp)==count:
               for j in range(1, len(nums[i:k])):
                    if temp[j - 1] >= temp[j] or temp[j]!=temp[j-1]+1:
                        res.append(-1)
                        indi = False
                        break
                   
                     
               if indi:
                    res.append(max(temp))
                  
            
            k += 1

        return res
