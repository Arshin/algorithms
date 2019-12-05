# Q: How do you find the largest and smallest number in an unsorted integer array?
class Solution:
    def func(self, nums):
        smallest = nums[0]
        largest = nums[0]
        secondSmallest = None
        secondLargest = None
        for num in nums:
            if num < smallest:
                secondSmallest = smallest
                smallest = num
            elif num > largest:
                secondLargest = largest
                largest = num

        return smallest, largest, secondSmallest, secondLargest


tmp = Solution()
print(tmp.func([1,2,4,5,5,6,7,9,10,0,1,1]))
