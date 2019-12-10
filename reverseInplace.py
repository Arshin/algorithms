class Solution:
    def reverseInplace(self, arr):
        return arr[::-1]


if __name__ == "__main__":
    tmp = Solution()
    print(tmp.reverseInplace([1,2,3,3,4,5,6,6,7,8,9,9]))
