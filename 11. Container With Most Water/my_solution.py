class Solution:
    def maxArea(self, height):
        '''
        brute force
        '''
        l = len(height)
        water = []
        for i in range(l):
            for j in range(i+1, l):
                water.append((j-i)*min([height[i], height[j]]))
        return max(water)

    def maxArea2(self, height):
        '''
        better than brute force,
        still O(n2) though
        and is over the time limit
        '''
        sorted_height = sorted(set(height))
        water = []
        top_idx_buff = []
        for i in reversed(sorted_height):
            top_level = i
            top_idx = [j for j, x in enumerate(height) if x>=top_level]
            # print([top_level, top_idx, top_idx_buff, water])
            if len(top_idx) >= 2:
                if not top_idx_buff or top_idx[0] < top_idx_buff[0] or top_idx[-1] > top_idx_buff[-1]:
                    water.append((top_idx[-1]-top_idx[0])*top_level)
                    top_idx_buff = top_idx
        return max(water)

    def maxArea3(self, height):
        '''
        it took me a life to finally come up with so many
        wrong answers...
        shxt
        '''
        l = len(height)
        pnt1, pnt2 = 0, l-1
        water = []
        while pnt1 < pnt2:
            print([pnt1, pnt2, water])
            water.append((pnt2-pnt1)*min([height[pnt1], height[pnt2]]))
            i = 1
            while i < l-pnt1-1 and height[pnt1] >= height[pnt1+i]:
                i += 1
            water.append((pnt2-pnt1-i)*min([height[pnt1+i], height[pnt2]]))
            water.append(i*height[pnt1])
            j = 1
            while j < pnt2 and height[pnt2] >= height[pnt2-j]:
                j += 1
            water.append((pnt2-j-pnt1)*min([height[pnt1], height[pnt2-j]]))
            water.append(j*height[pnt2])
            pnt1 += i
            pnt2 -= j
            #
            # i = 1
            # while i < min([l-pnt1-1, pnt2]) and height[pnt1] >= height[pnt1+i] and height[pnt2] >= height[pnt2-i]:
            #     i += 1
            #     print(i)
            # if height[pnt1] < height[pnt1+i]:
            #     water.append(i*height[pnt1])
            #     pnt1 += i
            # elif height[pnt2] < height[pnt2-i]:
            #     water.append(i*height[pnt2])
            #     pnt2 -= i
            # else:
            #     pnt1 += i
            #     pnt2 -= i
        return max(water)
