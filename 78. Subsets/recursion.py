class Solution:
    def subsets(self, nums):
        subset = []
        n = len(nums)

        def helper(i, tmp):
            subset.append(tmp)
            print(subset)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return subset

        # def backtrack(first = 0, curr = []):
        #     # if the combination is done
        #     if len(curr) == k:
        #         output.append(curr[:])
        #         # print(output)
        #     for i in range(first, n):
        #         # add nums[i] into the current combination
        #         curr.append(nums[i])
        #         # use next integers to complete the combination
        #         # print('curr before backtracking: '+str(curr))
        #         backtrack(i + 1, curr)
        #         # backtrack
        #         # print('curr after backtracking: '+str(curr))
        #         curr.pop()
        #
        # output = []
        # n = len(nums)
        # for k in range(n + 1):
        #     backtrack()
        # return output


'''
[]
[1] __ [1,2] __ [1,2,3] __ [1,2,3,4]
    __ [1,3] __ [1,3,4]
    __ [1,4]
[2] __ [2,3] __ [2,3,4]
    __ [2,4]
[3] __ [3,4]
'''
