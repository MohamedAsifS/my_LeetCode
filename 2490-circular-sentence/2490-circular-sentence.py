class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        sen=sentence.split(" ")
        if len(sen)==1:
            return False
        prev=sen[0][-1]

        for i in range(1,len(sen)):
            if prev != sen[i][0]:
               
                return False
            prev=sen[i][-1]
        return True
        