import sys
class Solution:
    def longestPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        minStr = min(strs, key=len)
        i = len(minStr)
        counter = 0

        while i > 0:
            for j in range(len(strs)):
                if minStr[:i] in strs[j][:i:]:
                    counter += 1
                    if counter == len(strs):
                        return minStr[:i]
            i -= 1
            counter = 0
        return ""
if __name__ == "__main__":
    tmp = Solution()
    print(tmp.longestPrefix(["Arshia", "Aria", "Arian"]))
