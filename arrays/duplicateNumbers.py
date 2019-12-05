# Q: How do you find the duplicate number on a given integer array?
class Solution:
    def func(self, nums):
        nums = sorted(nums)
        repeated = []
        for i in range(len(nums)):
            if nums[i]-nums[i-1]==0 and nums[i] not in repeated:
                repeated.append(nums[i])
        return repeated
        # return [nums[i] for i in range(len(nums)) if nums[i]-nums[i-1]==0]


tmp = Solution()
print(tmp.func([1,2,4,5,5,6,7,9,10,0,1,1]))
