# sqrt of num
class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num

        start = 0
        end = num

        while start<=end:
            mid = (start + end) //2

            if mid*mid == num:
                return mid

            if mid*mid < num:
                start += 1
                ans = mid

            else:
                end = mid - 1

        return ans

if __name__ == "__main__":
    tmp = Solution()
    print(tmp.func(15))
