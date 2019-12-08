class Solution:
    def removeDuplicates(self, arr):
        pointer = 0
        for j in range(1, len(arr)):
            if arr[pointer] !=  arr[j]:
                pointer+=1
                arr[pointer] = arr[j]
        else:
            return arr[:pointer+1]

if __name__ == "__main__":
    tmp = Solution()
    print(tmp.removeDuplicates([1,2,3,3,4,5,6,6,7,8,9,9]))
