class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        # if n == 0 or n == 1 or n == 2: return 0
        left_max, right_max = [0], [0]
        for i in range(1, n):
            left_max.append(max([left_max[i-1], height[i-1]]))
            right_max.append(max([right_max[i-1], height[n-i]]))
        right_max = right_max[::-1]

        for i in range(1, n):
            water += max([min([left_max[i], right_max[i]]) - height[i], 0])
        return water
