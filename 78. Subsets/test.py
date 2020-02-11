from my_solution import Solution as sol1
from recursion import  Solution as sol2
from iteration import  Solution as sol3

def main():
    nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    # ret = sol1().subsets(nums)
    ret = sol2().subsets(nums)
    # ret = sol3().subsets(nums)
    out = str(ret);
    print(out)

if __name__ == '__main__':
    main()
