class Solution(object):
    def reverse(self, s):
        result = 0

        if s < 0:
            symbol = -1
            s = -s
        else:
            symbol = 1

        while s:
            result = result * 10 + s % 10
            s /= 10

        return 0 if result > pow(2, 31) else result * symbol
