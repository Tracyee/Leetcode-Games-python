class Solution:
    # verision 1
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

    # version 2
    def reconstructQueue(self, people):
        d = {}
        for h, k in people:
            if h not in d:
                d[h] = [[h, k]]
            else:
                d[h].append([h, k])

        re = []
        for h in sorted(d.keys(), reverse=True):
            group = sorted(d[h])
            if not re:
                re += group
            else:
                for h, k in group:
                    re.insert(k, [h, k])

        return re
