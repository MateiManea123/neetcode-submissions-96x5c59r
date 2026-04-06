class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            elif temperatures[stack[-1]]>=temp:
                stack.append(i)
            else: 
                while stack and temp>temperatures[stack[-1]]:
                    j = stack.pop()
                    result[j] = i-j
                stack.append(i)
        
        return result
                
                
