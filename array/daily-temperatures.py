class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        ret = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while len(stack)>0 and temperatures[i]>temperatures[stack[len(stack)-1]]:
                ret[stack[len(stack)-1]] = i-stack[len(stack)-1]
                stack = stack[:-1]
            stack.append(i)
        return ret
        