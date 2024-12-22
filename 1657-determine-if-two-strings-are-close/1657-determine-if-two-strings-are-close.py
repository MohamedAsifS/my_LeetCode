class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False

        count1={}
        count2={}

        for i in word1:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        for i in word2:
            if i not in count2:
                count2[i]=1
            else:
                count2[i]+=1
        return count1.keys()==count2.keys() and sorted(count1.values())==sorted(count2.values())
        
            
        