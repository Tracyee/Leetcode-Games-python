class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        # concatenation
        def dfs1(target, index, path):
            if target == 0:
                res.append(path)
                return
            for i in range(index, n):
                if target - candidates[i] < 0:
                    break
                dfs(target-candidates[i], i, path+[candidates[i]])

        # append/pop
         def dfs2(target, index, path):
            if target == 0:
                res.append(path[:]) # notice the difference here
                return
            for i in range(index, n):
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                dfs(target-candidates[i], i, path)
                path.pop()

        dfs1(target, 0, [])
        # dfs2(target, 0, [])
        return res
