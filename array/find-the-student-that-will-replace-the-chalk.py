class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        new = k % sum(chalk)
        for i in range(0, len(chalk)):
            if new<chalk[i]:
                return i
            else:
                new-=chalk[i]
                