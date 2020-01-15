class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        self.result = []
    def sub(self):
        for i in range(len(self.nums)):
            result = self.target - self.nums[i]
            if result in self.nums: # if true, answers found!
                return [i, self.nums.index(result)]

def main():
    # n = int(input("Please specify the number of elements: "))
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    # nums.append(int(input("Please type ")))
    target = int(input("Please type your target as an integer: "))
    sol = Solution.twoSum(nums, target)
    print(sol.sub())

if __name__ == "__main__":
    main()
