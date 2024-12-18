class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]

        for i in image:
            temp=i[::-1]
            for i in range(len(temp)):
                if temp[i]==1:
                    temp[i]=0
                else:
                    temp[i]=1

            res.append(temp)
        return res
        