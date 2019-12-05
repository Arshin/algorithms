# Q: find the missing number in array of 1 to 100
class Solution:
    def missing(self, nums):
        nums = sorted(nums)
        actualSum = sum(nums)
        expectedSum = sum(range(nums[0], nums[-1]+1))
        return expectedSum - actualSum

tmp = Solution()
print(tmp.missing([1,2,4,5,6,7,8,9,10]))
