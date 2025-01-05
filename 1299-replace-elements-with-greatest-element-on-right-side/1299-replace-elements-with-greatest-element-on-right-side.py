class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
                if len(arr)==1:
                    return [-1]
             
                arr=arr[1:]
                maxi=-1
                for i in range(len(arr)-1,-1,-1):
                     
                     maxi=max(maxi,arr[i])
                     arr[i]=maxi
                 
                arr.append(-1)
                return arr
       
        