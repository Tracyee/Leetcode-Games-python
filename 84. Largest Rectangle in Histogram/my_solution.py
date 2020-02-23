class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        brute force
        '''
        if not heights: return 0
        n = len(heights)
        area = []
        for i in range(n):
            min_h = heights[i]
            for j in range(i, n):
                min_h = min([min_h, heights[j]])
                area.append(min_h * (j - i + 1))
        return max(area)

    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        optimize
        '''
        if not heights: return 0
        n = len(heights)
        area = []
