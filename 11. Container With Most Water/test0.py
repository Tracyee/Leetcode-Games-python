from my_solution import Solution as sol1
from twoPointer import Solution as sol2
from time import time

def main():
    # nums = list(map(int, input("Please tpye your choice of integers: ").split()))
    import pickle
    with open('input.data', 'rb') as filehandle:
    # read the data as binary data stream
        nums = pickle.load(filehandle)
    start_time = time()
    ret = sol1().maxArea2(nums)
    # ret = sol2().maxArea(nums)
    end_time = time()
    print(str(ret))
    print(str(end_time-start_time))

if __name__ == '__main__':
    main()
