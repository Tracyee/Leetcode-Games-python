class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pnt1 = pnt2 = 0
        n = len(s)
        longest = 0
        combo = {}
        while pnt2 < n:
            if s[pnt2] in combo:
                pnt1 = max([combo[s[pnt2]] + 1, pnt1])
            combo[s[pnt2]] = pnt2
            pnt2 += 1
            longest = max([longest, pnt2-pnt1])
        return longest
