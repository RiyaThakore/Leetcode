class Solution(object):
    def isIsomorphic(self, s, t):
        seen = {}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in seen.keys():
                    if t[i] not in seen.values():
                        seen[s[i]]=t[i]
                    else:
                        return False
                else:
                    if seen[s[i]]!=t[i]:
                        return False
                        break
            return True
