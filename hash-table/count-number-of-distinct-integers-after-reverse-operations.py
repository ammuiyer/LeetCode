class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        #add everthing to a set
        s = set()
        for item in nums:
            s.add(item)
            rev = int(str(item)[::-1])
            s.add(rev)
        return len(s)

        