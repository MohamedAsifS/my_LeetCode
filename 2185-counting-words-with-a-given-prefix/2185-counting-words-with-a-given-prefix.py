class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        res=0

        for i in words:
            if i[0:len(pref)]==pref:
                res+=1
        return res
        