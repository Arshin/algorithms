class Solution:
    def reverseString(self, s):
        # using array
        # return = s[::-1]
        # Brute
        rev = ''
        for ind in range(len(s)):
            rev+=s[len(s)-ind-1]
        return rev

tmp = Solution()
print(tmp.reverseString('Arash'))
