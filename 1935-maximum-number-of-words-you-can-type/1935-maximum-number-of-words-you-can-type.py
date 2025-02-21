class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split(" ")
        check=[]
        for i in text:
            check.append(set(i))
        res=0
        for i in text:
            count=True
            for j in brokenLetters:
                if j in i:
                    count=False

                    break
            if count:
                res+=1
        return res
        