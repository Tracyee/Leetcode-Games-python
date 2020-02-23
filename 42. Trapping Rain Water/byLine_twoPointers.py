class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        left_max = right_max = 0
        p1, p2 = 0, n-1
        while p2 > p1:
            if height[p1] < height[p2]:
                water += max([left_max - height[p1], 0])
                left_max = max([left_max, height[p1]])
                p1 += 1
            else:
                water += max([right_max - height[p2], 0])
                right_max = max([right_max, height[p2]])
                p2 -= 1
        return water
