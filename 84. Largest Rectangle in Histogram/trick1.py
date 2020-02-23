class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        For each bar i, we look for the first bar left_i on the left that is
        lower than bar[i] and the first bar right_i on the right that is lower
        than bar[i]. Then the largest size determined by bar[i]
        (bar[i] as the peak) is height[i] * (right_i - left_i - 1)
        '''
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res
