class Solution:
    def func(self, array):
        if len(array) < 1:
            return peint("too small, size matters!")
        dic = dict()
        max_freq = 0
        frequent = None
        for elem in array:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem]+=1
            if dic[elem] > max_freq:
                max_freq = dic[elem]
                frequent = elem

        return frequent


tmp = Solution()
print(tmp.func([0,0,2,2,3,4,1,1,1,1,4,5,6,6,7,7]))
