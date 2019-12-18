class Solution:
    def func(self, s):
        s = s.replace(' ', '').lower()

        dic = dict()
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        # for char in s:
        #     if dic[char] == 1:
        #         return char

        return (sorted(dic.items(), key= lambda x:x[1]))


tmp = Solution()
print(tmp.func("Arash"))
