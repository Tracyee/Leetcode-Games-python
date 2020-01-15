class Solution:
    def twoSum(self, nums, target):
        buff = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in buff: # if true, answers found!
                return [buff[result], i]
            else:
                buff[nums[i]] = i


def main():
    # n = int(input("Please specify the number of elements: "))
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    # nums.append(int(input("Please type ")))
    target = int(input("Please type your target as an integer: "))
    sol = Solution().twoSum(nums, target)
    print(sol)

if __name__ == "__main__":
    main()
