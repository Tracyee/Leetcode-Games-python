class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        max_height = max(height)
        for i in range(1, max_height+1):
            is_start = False
            tmp = 0
            for j in range(len(height)):
                if is_start and height[j] < i:
                    tmp += 1
                if height[j] >= i:
                    water += tmp
                    tmp = 0
                    is_start = True
        return water
