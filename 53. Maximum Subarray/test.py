from my_solution import Solution as sol1
from kadane import Solution as sol2


def main():
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    # ret = sol1().maxSubArray(nums)
    ret = sol2().maxSubArray(nums)
    out = str(ret);
    print(out)

if __name__ == '__main__':
    main()
