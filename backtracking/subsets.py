class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        for num in nums:
            temp = []
            for x in s:
                xcopy = [z for z in x]
                xcopy.append(num)
                temp.append(xcopy)
            [s.append(r) for r in temp]
        return s


        