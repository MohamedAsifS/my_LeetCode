class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        to=k%n
        rotated=[0]*n
        if to==n:
            return nums
        # while to>0:
        #     val=nums.pop()
        #     nums.insert(0,val)
        #     to-=1
        #above code will work effiecent but more effiecent in python is using ib-built function
        # nums.reverse()
        # nums[:to]=reversed(nums[:to])
        # nums[to:]=reversed(nums[to:])

        
        # up both is good but we need more effiecent one 
        print(to)
        for i in range(n):
            rotated[(i+to) % n] = nums[i]
            print((i+to) % n)
        for i in range(n):
            nums[i]= rotated[i]



        