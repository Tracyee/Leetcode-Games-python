from my_solution import Solution as sol1
from recursion_swap import Solution as sol2

def main():
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    # ret = sol1().permute(nums)
    ret = sol2().permute(nums)
    out = str(ret);
    print(out)

if __name__ == '__main__':
    main()
