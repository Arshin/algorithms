class Solution:
    def palindrome(self, x):
        org = x
        rev = 0
        while x > rev:
            rev = rev*10 + x%10
            x /= 10
        if (rev == x) or (rev/10 == x):
            return (rev, True)
        else:
            return (rev, False)

tmp = Solution()
print(tmp.palindrome(156751))
