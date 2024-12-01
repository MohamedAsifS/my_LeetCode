class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashp={}
    

        for i in range(len(arr)):
            temp=arr[i]*2
            div=arr[i]/2
            if temp in hashp or div in hashp:
                print(hashp)
                print(arr[i])
                return True
            else:
                hashp[arr[i]]=temp
                
   
        return False

        