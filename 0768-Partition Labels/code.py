class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hash={}

        for i in range(len(s)):
            hash[s[i]]=i
        print(hash)    

        check=-1 
        res=[] 
        start=0
        for i in range(len(s)):
            check=max(check,hash[s[i]])

            if i == check:
                res.append((i-start)+1)
                start=i+1
        return res
