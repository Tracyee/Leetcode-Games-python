class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        nums_dict = {}
        for i in range(length):
            if i in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        majority_ele = max(nums_dict, key=nums_dict.get)
        return majority_ele
