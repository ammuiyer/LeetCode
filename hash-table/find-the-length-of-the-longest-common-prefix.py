class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ma = 0
        for i in list(set(arr1)):
            for j in list(set(arr2)):
                a = str(i)
                b = str(j)
                count = 0
                for x,y in zip(a,b):
                    if x==y:
                        count+=1
                    else:
                        break
                ma = max(ma, count)
        return ma
                    
                

        