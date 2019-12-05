# Q: find missing numbers in array of 1 to n
class Solution:
    def missing(self, nums):
        nums = sorted(nums)
        start = nums[0]
        end = nums[-1]+1
        return [x for x in range(start,end) if x not in nums]

tmp = Solution()
print(tmp.missing([1,2,4,5,6,7,9,10]))
