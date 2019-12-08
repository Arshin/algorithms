class Solution:
    def strstr(self, s, needle):
        lenNeedle = len(needle)
        i = 0
        while i < len(s):
            if s[i:i+lenNeedle] == needle:
                return i
            i+=1
        return -1




if __name__ == "__main__":
    tmp = Solution()
    print(tmp.strstr('hello', 'll'))
