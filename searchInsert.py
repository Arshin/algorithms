class Solution:
    def searchInsert(self, nums, target):
        for j in range(len(nums)):
            if target <= nums[j]:
                 return j
        return len(nums)




if __name__ == "__main__":
    tmp = Solution()
    print(tmp.strstr('hello', 'll'))
