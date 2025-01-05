class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
                if len(arr)==1:
                    return [-1]
                res=[]
                arr=arr[1:]
                maxi=arr[-1]
                for i in range(len(arr)-1,-1,-1):
                     
                     maxi=max(maxi,arr[i])
                     res.append(maxi)
                res=res[::-1]   
                res.append(-1)
                return res
       
        