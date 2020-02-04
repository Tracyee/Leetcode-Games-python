class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        water = []
        while l < r:
            water.append((r-l)*min([height[l], height[r]]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max(water)
