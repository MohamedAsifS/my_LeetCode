class Solution:
    def convertDateToBinary(self, date: str) -> str:

        w=date.split("-")
        res=""
        print(w)
        for i in w:
            res+=bin(int(i))[2:]
            res+="-"
          
          
        return res[:-1]

        