from my_solution import Solution as sol1
from twopointers_backwds import Solution as sol2


def main():
    nums1 = list(map(int, input("Please tpye your choice of integers for nums1: ").split()))
    nums2 = list(map(int, input("Please tpye your choice of integers for nums2: ").split()))
    m = int(input("Please choose your m as the number of elements initialized in nums1"))
    m = int(input("Please choose your n as the number of elements initialized in nums2"))
    ret = sol1().merge(nums1, m, nums2, n)
    # ret = sol2().merge(nums1, m, nums2, n)
    out = str(nums1);
    print(out)

if __name__ == '__main__':
    main()
