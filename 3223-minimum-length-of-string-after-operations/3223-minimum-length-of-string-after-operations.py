class Solution:
    def minimumLength(self, s: str) -> int:

        res=len(s)

        f=Counter(s)
        print(f)
        for i in f.values():
            if i%2 == 0:
                res-=(i-2)
            elif  i%2 != 0:
                res-=(i-1)
        return res        