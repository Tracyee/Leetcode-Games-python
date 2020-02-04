from my_solution import Solution as sol1
# from twoPointers import Solution as sol2


def main():
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    ret = sol1().threeSum(nums)
    # ret = sol2().removeDuplicates(nums)
    out = str(ret);
    print(out)

if __name__ == '__main__':
    main()
