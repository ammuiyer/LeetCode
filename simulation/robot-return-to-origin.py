class Solution:
    def judgeCircle(self, moves: str) -> bool:
        curr = [0, 0]
        for move in moves:
            if move == 'R':
                curr[1]+=1
            if move == 'L':
                curr[1]-=1
            if move == 'U':
                curr[0]+=1
            if move == 'D':
                curr[0]-=1
        return curr==[0,0]
                  
        