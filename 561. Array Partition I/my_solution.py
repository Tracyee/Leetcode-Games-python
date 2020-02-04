class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# a math problem
# the difference of ai and bi is the "loss"
# we want to make the "loss" as small as possible
# sort the array and the resulting array is fine enough
# to solve the problem
