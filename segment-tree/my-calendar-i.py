class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        
        self.intervals.sort(key = lambda x:x[0])
        for i in range(0, len(self.intervals)):
            # print(self.intervals[i])
            if self.intervals[i][0]>start:
                if i!=0 and self.intervals[i-1][1]>start:
                        return False
                if i==0 and self.intervals[i][0]<end:
                    return False
            if self.intervals[i][1]>start:
                return False



        self.intervals.append([start, end])
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)