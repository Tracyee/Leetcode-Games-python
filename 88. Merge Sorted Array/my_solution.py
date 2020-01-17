class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2[0:n]
        # if num1[m-1] > num1[m]:
        #     num1[m-1], num1[m] = num1[m], num1[m-1]
        #     if num1[m] > num1[m+1]:
        #         num1[m+1], num1[m] = num1[m], num1[m+1]
        #         if num1[m-2] > num1[m-1]:
        #             num1[m-1], num1[m-2] = num1[m-2], num1[m-1]
        nums1.sort()
