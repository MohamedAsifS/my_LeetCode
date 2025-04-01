class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        hash={}

        for i in s:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1

        prev=0
        for i in hash:
            if prev == 0:
                prev=hash[i]
            elif prev!=hash[i]:
                return False

            prev=hash[i]
        return True


        