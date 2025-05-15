class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for i in strs:
            stock=[0]*26
            for j in i:
              
                stock[ord(j)-97]+=1
            res[tuple(stock)].append(i)
     

        return list(res.values())
        