class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        right=Counter(s)
        left=set()

        for m in s:
            right[m]-=1

            for c in left:
                if right[c]>0:
                    res.add((m,c))
            left.add(m)
        return len(res)        