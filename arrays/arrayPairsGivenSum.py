# Q: How do you find the largest and smallest number in an unsorted integer array?
class Solution:
    def func(self, nums, target):
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and [nums[i], nums[j]] not in pairs:
                    pairs.append([nums[i], nums[j]])
        return pairs


tmp = Solution()
print(tmp.func([1,2,4,5,4,1,9,10,0], 10))
