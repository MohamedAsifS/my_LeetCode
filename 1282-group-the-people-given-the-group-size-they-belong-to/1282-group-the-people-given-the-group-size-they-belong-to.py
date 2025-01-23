class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashed={}
        res=[]

        for i in range(len(groupSizes)):
            if groupSizes[i] not in hashed:
                hashed[groupSizes[i]]=[]
                hashed[groupSizes[i]].append(i)
            elif groupSizes[i] in hashed and len(hashed[groupSizes[i]]) < groupSizes[i]  :
                 hashed[groupSizes[i]].append(i) 
            else:
                res.append(hashed[groupSizes[i]])
                hashed[groupSizes[i]]=[]
                hashed[groupSizes[i]].append(i)

        for i in hashed.values():
            res.append(i)
        return res
       
