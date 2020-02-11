class Solution:
    def subsets(self, nums):
        subset = [[]]
        for i in nums:
            subset += [[i] + num for num in subset]
            print(subset)
        return subset


'''
[]
+ [1]
+ [2] [2,1]
+ [3] [3,1] [3,2] [3,2,1]
+ [4] [4,1] [4,2] [4,2,1] [4,3] [4,3,1] [4,3,2] [4,3,2,1]
'''
