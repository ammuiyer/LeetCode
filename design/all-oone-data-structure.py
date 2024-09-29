class AllOne:

    def __init__(self):
        self.max = ""
        self.maxcount = 0
        self.min = ""
        self.mincount = 100000
        self.strings = {}
        

    def inc(self, key: str) -> None:
        if key in self.strings:
            self.strings[key]+=1
            if self.strings[key]>self.strings[self.max]:
                self.maxcount = self.strings[key]
                self.max = key
            if self.strings[key]==self.strings[self.min]:
                self.min = ""
            if len(self.strings)==1:
                self.min = key
        else:
            self.strings[key]=1  
            if self.max=="":
                self.max = key
                self.maxcount = 1 
            if self.min=="":
                self.min = key
                self.mincount = 1
            if self.strings[self.min]>1:
                self.min = key


    def dec(self, key: str) -> None:
        self.strings[key]-=1
        if self.strings[key]==0:
            del self.strings[key]
            if key==self.max:
                self.max=""
        else: 
            if key==self.max:
                self.max = ""
        

    def getMaxKey(self) -> str:
        return self.max
        

    def getMinKey(self) -> str:
        return self.min
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()