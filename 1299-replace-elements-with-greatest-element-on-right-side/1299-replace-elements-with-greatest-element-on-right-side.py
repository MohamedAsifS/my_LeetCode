class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
                 res=[]
                 arr=arr[1:]
                 for i in range(len(arr)):
                     res.append(max(arr[i:]))
                 res.append(-1)
                 return res
       
        