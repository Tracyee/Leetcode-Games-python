class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1[m:m+n] = num2[0:n]
        # if num1[m-1] > num1[m]:
        #     num1[m-1], num1[m] = num1[m], num1[m-1]
        #     if num1[m] > num1[m+1]:
        #         num1[m+1], num1[m] = num1[m], num1[m+1]
        #         if num1[m-2] > num1[m-1]:
        #             num1[m-1], num1[m-2] = num1[m-2], num1[m-1]
        num1.sort()
