class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs)<1:
            return 0
        count = 0
        for i in range(0, len(strs[0])):
            temp = []
            temp2 = []
            for j in range(0, len(strs)):
                temp.append(strs[j][i])
                temp2.append(strs[j][i])
            print(temp, temp2)
            temp.sort()
            if temp != temp2:
                count+=1
        return count
        