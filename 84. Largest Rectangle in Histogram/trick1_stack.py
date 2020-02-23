class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        maintain a monotonic increasing stack to find the left_i and
        right_i
        '''
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
