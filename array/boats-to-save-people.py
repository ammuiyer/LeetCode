class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l, r, count = 0, len(people)-1, 0
        while(l<=r):
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            else:
                #move right till valid
                r-=1
            count+=1
        return count