from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Use a stack that keeps track of temps, and the day they were seen 
        output = [0 for i in range(len(temperatures))]
        stack = []

        # Go through each daily temp
        for i in range(len(temperatures)):

            temp = temperatures[i]

            # If we have a temp that is greater than the one on the top of the stack,
            # we can calculate the number of days that have passed based on that values
            # paired index. So we update that index in the output list, and keep
            # popping while out curr temp is bigger. Then add the curr to start again. 
            while stack != [] and temp > stack[-1][0]:
                print(i - stack[-1][1])
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append([temp, i])

        return output