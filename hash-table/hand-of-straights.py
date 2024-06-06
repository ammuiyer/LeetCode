class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        d = {}
        for x in hand:
            if x not in d:
                d[x] = 1
            else:
                d[x]+=1
        for i in range(len(hand)//groupSize):
            curr = min(d.keys())
            for j in range(groupSize):
                if curr not in d:
                    return False
                d[curr]-=1
                if d[curr]==0:
                    del d[curr]
                curr+=1
        return True
        
        