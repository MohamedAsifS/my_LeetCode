class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        #first substaring

        # checker={'a','e','i','o','u'}
        # const=0
        # prime=0
        # res=0
        # for i in range((5+k)):
        #     if word[i] in checker:
        #         prime+=1
        #     else:
        #         const+=1
        # if prime==5 and const ==k:
        #     res+=1
        # print(res)
        # l=0

        # for r in range(5+k,len(word)):
            
        #     print(prime,const)
        #     if word[r] not in checker:
        #         const+=1
        #     else:
        #         prime+=1
            
        #     if word[l] not in checker:
        #         const-=1
        #     else:
        #         prime-=1
        #     l+=1
        #     if prime>=5 and const==k:
        #         res+=1
        
        #solution is from neetcode

        def countk(k):
            l=0
            res=0
            con=0
            di=defaultdict(int)

            for r in range(len(word)):
                if word[r] in 'aeiou':
                    di[word[r]]+=1
                else:
                    con+=1
                while len(di)>=5 and con >=k:
                    res+=(len(word)-r)
                    if word[l] in 'aeiou':
                        di[word[l]]-=1
                    else:
                        con-=1
                    if di[word[l]]==0:
                        di.pop(word[l])
                    l+=1
            return res


           
        return countk(k) - countk(k+1)
        