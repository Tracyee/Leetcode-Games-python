class Solution:
    def trap(self, height: List[int]) -> int:
        p1, p2 = 0, 1
        n = len(height)
        water = [0]
        while p2 < n:
            if height[p2] >= height[p1]:
                water.append((p2 - p1 - 1) * height[p1])
                p1 = p2
            p2 += 1
        return water

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        p1, p2 = 0, 1
        n = len(height)
        water = [0]
        # left = [[p1, height[p1]]]
        left = []
        while p2 < n:
            if height[p1] > height[p2]:
                left.append([p1, height[p1]])
            elif height[p1] < height[p2]:
                while left:
                    buff_p, buff_h = left.pop()
                    water.append((p2-buff_p-1)*(min([buff_h, height[p2]])-max([height[buff_p+1], height[p1]])))
                    if buff_h == height[p2]: break
                    if buff_h > height[p2]:
                        left.append([buff_p, buff_h])
                        break
            p1 += 1
            p2 += 1
            print(water)
        return sum(water)
