class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items=sorted(items,key=lambda x : x[1],reverse=True)

        
        res=[]
        for i in queries:
            check=True
            for j in items:
                if j[0]<=i:
                    res.append(j[1])
                    check=False
                    break
            if check:
                res.append(0)
        return res
             

        
        