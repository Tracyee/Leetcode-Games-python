class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        just avoid inserting a number after any of its duplicates
        hence, change the range(len(pin)+1) to range((r+[pin]).index(pin)+1)
        '''
        res = [[]]

        for pin in nums:
            res = [r[:i]+[pin]+r[i:] for r in res for i in range((r+[pin]).index(pin)+1)]
            # print(res)

        return res
