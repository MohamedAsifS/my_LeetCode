class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        state={}

        for i in arr:
            if i not in state:
                state[i]=1
            else:
                state[i]+=1
        value=list(state.values())
      
        if len(set(value))!=len(value):
            return False
        else:
            return True
        