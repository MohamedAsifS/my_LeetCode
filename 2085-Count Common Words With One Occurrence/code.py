class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hash1={}
        for i in words1:
            if i not in hash1:
                hash1[i]=1
            else:
                hash1[i]+=1
        hash2={}
        for i in words2:
            if i not in hash2:
                hash2[i]=1
            else:
                hash2[i]+=1
        count=0
        for i in hash1:
            if hash2.get(i,0)==1 and hash1.get(i)==1:
                count+=1 
        return count
        