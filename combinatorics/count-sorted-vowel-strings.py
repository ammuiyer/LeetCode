class Solution:
    def countVowelStrings(self, n: int) -> int:
        M = [1,1,1,1,1]
        for i in range(1, n):
            temp = [x for x in M]
            for j in range(5):
                for k in range(j+1, 5):
                    M[k]+=temp[j]
        sum = 0
        for x in M:
            sum+=x
        return sum

            

        