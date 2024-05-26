class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        for num in nums:
            temp = []
            for x in s:
                xcopy = [z for z in x]
                xcopy.append(num)
                xcopy.sort()
                temp.append(xcopy)
            for r in temp:
                if r not in s:
                    s.append(r) 
        return s
        