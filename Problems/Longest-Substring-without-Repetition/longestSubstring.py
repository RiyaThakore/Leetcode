class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cur, l, start = 0,0,0
        N = len(s)
        i = 0
        lookup = {}
        while i < N:
            if s[i] not in lookup:
                cur+=1
            else:
                start = max(start, lookup[s[i]])
                cur = i - start
            lookup[s[i]] = i
            l = max(cur, l)
            i+=1
        return l
