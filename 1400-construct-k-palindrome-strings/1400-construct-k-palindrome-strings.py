class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False
        
        c = Counter(s)
        odd_count = 0
        for i in c.values() :
            odd_count += i % 2
        return odd_count <= k
         