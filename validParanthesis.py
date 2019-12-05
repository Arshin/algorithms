class Solution:
    def isValid(self, s):
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in mapping:
                topelement = stack.pop() if stack else False
                if topelement != mapping[char]:
                    return False
            else:
                stack.append(char)

        print(stack)
        return not stack


tmp = Solution()
print(tmp.isValid("({({[[((()))]]})})"))
