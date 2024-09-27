class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.doubles = []

    def book(self, start: int, end: int) -> bool:
        
        for i in range(0, len(self.doubles)):
            # print(self.intervals[i])
            if  (max(start,self.doubles[i][0]) < min(end,self.doubles[i][1])):
                return False

        for i in range(0, len(self.intervals)):
            # print(self.intervals[i])
            if  (max(start,self.intervals[i][0]) < min(end,self.intervals[i][1])):
                self.doubles.append([max(start, self.intervals[i][0]), (min(end, self.intervals[i][1]))])


        self.intervals.append([start, end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)