class Solution:
    def removeVal(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1

        return i



if __name__ == "__main__":
    tmp = Solution()
    print(tmp.removeVal([1,1,2,3,3], 3))
