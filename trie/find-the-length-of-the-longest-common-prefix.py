class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ma = 0
        d = {}
        d["1"] = []
        d["2"] = []
        d["3"] = []
        d["4"] = []
        d["5"] = []
        d["6"] = []
        d["7"] = []
        d["8"] = []
        d["9"] = []
        for i in list(set(arr1)):
            a = str(i)
            d[a[0]].append(a)
        for i in list(set(arr2)):
            a = str(i)
            for j in d[a[0]]:
                b = str(j)
                count = 0
                for x,y in zip(a,b):
                    if x==y:
                        count+=1
                    else:
                        break
                ma = max(ma, count)
        return ma
                    
                

        