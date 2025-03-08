class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white=blocks[0:k].count('W')
        black=k-white

        r=k
        res=white
        for l in blocks[0:len(blocks)-k]:
            if l=='B':
                black-=1
            elif l=='W':
                white-=1
            
            if blocks[r]=='B':
                black+=1
            elif blocks[r]=='W':
                white+=1
            r+=1
            res=min(white,res)
        return res

            

                 

        
        