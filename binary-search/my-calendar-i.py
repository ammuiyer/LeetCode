class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        
        self.intervals.sort(key = lambda x:x[0])
        for i in range(0, len(self.intervals)):
            # print(self.intervals[i])
            if  (end > self.intervals[i][0] and start < self.intervals[i][1]):
                return False



        self.intervals.append([start, end])
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)