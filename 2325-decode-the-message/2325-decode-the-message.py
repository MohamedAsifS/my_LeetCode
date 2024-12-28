class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        dic={}
        count=0
        for i in range(len(key)):
            if key[i] not in dic and key[i]!=" " and count<26:
                dic[key[i]]=a[count]
                count+=1
        res=""
        for i in message:
          if i ==" ":
                res+=i
          else:
            res+=dic.get(i)
        return res

        