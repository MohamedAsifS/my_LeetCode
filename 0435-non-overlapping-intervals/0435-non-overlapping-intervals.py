class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals=sorted(intervals,key=lambda x:x[1])
        print(intervals)
        res=0
        track=-4000000
        for i in intervals:
           if i[0]<track:
              
                res+=1
           else:
                track=i[1]
        return res
             
        