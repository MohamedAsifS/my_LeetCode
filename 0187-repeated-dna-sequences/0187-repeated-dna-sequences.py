class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
      
        hash={}
        res=set()
        l=10
      

        for i in range(0,len(s)-9):
            slices=s[i:l]
            if slices not in hash:
                hash[slices]=1
            else:
                hash[slices]+=1
                res.add(slices)
            l+=1
        return list(res)
        