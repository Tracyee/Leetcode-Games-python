class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        sort candidates if break is used.
        otherwise, uncomment line 13, 14

        '''
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(first=0, curr=[]):
            # print("now curr is: "+str(curr))
            # if sum(curr) > target:
            #     return
            if sum(curr) == target:
                res.append(curr)
                return
            for i in range(first, n):
                nex = curr + [candidates[i]]
                if sum(nex) > target:
                    break
                backtrack(i, nex)
                # print("backtrack")

        backtrack()
        return res

'''
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(first=0, curr_sum=0, curr=[]):
            # print("now curr is: "+str(curr))
            # if curr_sum > target:
            #     return
            if curr_sum == target:
                res.append(curr)
                return
            for i in range(first, n):
                if curr_sum + candidates[i] > target:
                    break
                backtrack(i, curr_sum + candidates[i], curr + [candidates[i]])
                # print("backtrack")

        backtrack()
        return res
'''
