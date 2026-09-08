class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        count = 0
        stack = []
        for i in range(0,len(temperatures)):
            current = temperatures[i]
            if len(stack)==0 or stack[-1][0] > current:
                stack.append((current,i))
            else:
                while stack and stack[-1][0] < current:
                    temp = stack.pop()
                    output[temp[1]] = i-temp[1]
                stack.append((current,i))
        return output





