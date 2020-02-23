class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_i = right_i = [0] * n
        left_i[0], right_i[-1] = -1, n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
            
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res
