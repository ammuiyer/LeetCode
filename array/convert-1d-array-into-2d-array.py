class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ret = []
        curr = []
        if m*n!=len(original):
            return ret
        for i in range(len(original)):
            if i%n==0 and i!=0:
                ret.append(curr)
                curr = [original[i]]
            else:
                curr.append(original[i])
        ret.append(curr)
        return ret
        