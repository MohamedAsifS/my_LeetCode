class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        num1=Counter(nums1)
        num2=Counter(nums2)
        res=[]
        count=0
        for i in nums2:
            if i in num1:
                count+=num1[i]
                del num1[i]
        res.append(count)
        count=0
        for i in nums1:
            if i in num2:
                count+=num2[i]
                del num2[i]
        res.append(count)

        return res

