class Solution:
    def countSegments(self, s: str) -> int:
        val=s.split(" ")
        count=0
        for i in val:
            if i!="":
                count+=1
        return count
        