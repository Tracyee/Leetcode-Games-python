class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(first=0, curr=[]):
            print("now curr is: "+str(curr))
            if sum(curr) == target:
                res.append(curr)
                return
            # used = []
            for i in range(first, n):
                nex = curr + [candidates[i]]
                if sum(nex) > target:
                    break
                # if candidates[i] not in used:
                #     backtrack(i+1, nex)
                #     # print("backtrack")
                # used.append(candidates[i])
                # # print("now used is: "+str(used))
                if i > first and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, nex)
                print("backtrack")
        backtrack()
        return res
