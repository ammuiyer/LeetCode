class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for item in tasks:
            if item in d:
                d[item] = (d[item][0]+1, 0)
            else:
                d[item] = (1, 0)
        ret = 0
        while len(d)>0:
            #pick a task that is available, the biggest task
            #print(d)
            sm = False
            maK = next(iter(d))
            maV = 0 
            for t in d.keys():
                if d[t][1]<=0:
                    #print("TE", t)
                    if d[t][0]>=maV:
                        sm=True
                        maV = d[t][0]
                        maK = t
            #decrease evertying's time by 1
            #print(maK, maV)
            for t in d.keys():
                    d[t] = (d[t][0], d[t][1]-1)
            if sm:
                #reset ttje chosen ones value to n
                d[maK] = (d[maK][0]-1, n)
                if d[maK][0]<=0:
                    del d[maK]
            ret+=1

        return ret
            
        
        