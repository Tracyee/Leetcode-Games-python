heights = [9,1,5,8,3,2,6,10]
stack = []
for i in range(len(heights)):
    print(stack)
    while stack and heights[stack[-1]] > heights[i]:
        stack.pop()
        # res = max(res, (i - stack[-1] - 1) * heights[tmp])
    stack.append(i)
