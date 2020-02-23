class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        # print(people)
        n = len(people)
        res = [None] * n
        same_cnt = 0
        for i in range(n):
            k = people[i][1]
            if i > 0 and people[i][0] == people[i-1][0]:
                same_cnt += 1
                k -= same_cnt
            count = j = 0
            while j < n and count <= k:
                if res[j] is None:
                    count += 1
                j += 1
            res[j-1] = people[i]
            if i < n-1 and people[i][0] != people[i+1][0]:
                same_cnt = 0
        return res
