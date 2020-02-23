class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pnt1 = pnt2 = 0
        n = len(s)
        longest = 0
        combo = {}
        while pnt2 < n:
            # print(combo)
            if s[pnt2] not in combo:
                combo[s[pnt2]] = pnt2
                pnt2 += 1
                longest = max([longest, pnt2-pnt1])
            else:
                pnt1 = combo[s[pnt2]] + 1
                for i in combo.copy():
                    if combo[i] < pnt1:
                        combo.pop(i)
        return longest

        def lengthOfLongestSubstring2(self, s: str) -> int:
        pnt1 = pnt2 = 0
        n = len(s)
        longest = 0
        combo = {}
        while pnt2 < n:
            # print(combo)
            if s[pnt2] not in combo:
                combo[s[pnt2]] = pnt2
                pnt2 += 1
                longest = max([longest, pnt2-pnt1])
            else:
                del combo[s[pnt1]]
                pnt1 += 1
        return longest
