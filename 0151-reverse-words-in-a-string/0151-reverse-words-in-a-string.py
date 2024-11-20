class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.split(" ")

        res=""

        for i in reversed(s):
            if i!="":
                res+=i
                res+=" "
        return res[:-1]
        