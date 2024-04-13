class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def bestMin(arr):
            arrs = []
            temp = []
            for i in range(0, len(arr)):
                if arr[i]==0:
                    arrs.append(temp)
                    temp = []
                else:
                    temp.append(arr[i])
            arrs.append(temp)
            currMax = 0
            for a in arrs:
                if len(a)>0:
                    for i in range(0, len(a)):
                        for j in range(i, len(a)):
                            currMax = max(min(a[i:j+1])*len(a[i:j+1]), currMax)
                    
            return currMax
        currMax, small=0, inf
        currArr = [0]*len(matrix[0])
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j]!="0":
                    currArr[j]+=1
                    
                if matrix[i][j]=="0":
                    currArr[j]=0
                    # print(j, currArr)
            
            currMax = max(currMax, bestMin(currArr))
            #print(currArr, bestMin(currArr))
            # print(currMax)
        return currMax
        
                    
                


        