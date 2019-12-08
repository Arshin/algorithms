class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1


if __name__ == "__main__":
    tmp = Solution()
    print(tmp.removeDumplicates([1,1,2,3,4,4,5]))
