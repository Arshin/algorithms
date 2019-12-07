class Solution:
    def palindrome(self, x):
        org = x
        rev = 0
        while x > rev:
            rev = rev*10 + x%10
            x /= 10
        if (rev == x) or (rev/10 == x):
            return (x, rev, True)
        else:
            return (x, rev, False)
# Test
tmp = Solution()
print(tmp.palindrome(182181))
