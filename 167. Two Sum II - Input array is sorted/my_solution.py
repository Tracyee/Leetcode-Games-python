class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        buff = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in buff: # if true, answers found!
                return [buff[result]+1, i+1]
            else:
                buff[nums[i]] = i
