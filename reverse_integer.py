import sys
class Solution:
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        rev = 0
        while x != 0:
            # pop
            pop = x%10
            x /= 10
            # push
            tmp = rev * 10 + pop
            rev = tmp
        if not neg:
            return rev
        else:
            return -rev

tmp = Solution()
print(tmp.reverse(-126))
