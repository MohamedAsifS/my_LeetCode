class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums1=1
        nums2=0

        while n !=0:
            digit=n%10
            nums1*=digit
            nums2+=digit
            n//=10
       
        return nums1-nums2
        
        