class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        res=[]

        for i in range(len(boxes)):
            temp=0
            for j in range(len(boxes)):

                    if boxes[j]=="1" and i!=j:
                        temp+=abs(i-j)
            res.append(temp)
        return res

        