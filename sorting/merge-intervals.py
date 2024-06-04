class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort
        intervals.sort(key=lambda x:x[0])
        i=0
        while i < len(intervals)-1:
            if intervals[i+1][0] <= intervals[i][1]:
                #combine
                intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                del intervals[i+1]
                
            else:

                i+=1
        return intervals 
            
        