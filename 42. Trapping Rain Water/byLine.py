class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            if i == 0: left_max = 0
            else:
                left_max = max(height[:i])
            if i == n-1: right_max = 0
            else:
                right_max = max(height[i+1:])
            water += max([min([left_max, right_max]) - height[i], 0])
        return water
