class Solution:
    def func(self, list1, list2):
        common = []
        for ind, val in enumerate(list1):
            if val in list2 and val not in common:
                common.append(val)

        return sorted(common)


tmp = Solution()
print(tmp.func([1,2,3,4,5,6,7,8], [1,22,33,44,5,66,7,88]))
