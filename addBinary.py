# add 2 binary strings
class Solution:
    def func(self, a, b):
        res = ''
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        tmp = 0
        for ind in range(max_len-1, -1, -1):
            tmp=carry
            tmp+=1 if a[ind] == '1' else 0
            tmp+=1 if b[ind] == '1' else 0
            res = ('1' if tmp%2==1 else '0') + res
            carry = 0 if tmp<2 else 1

        if carry != 0 : res = '1' + res

        return res

if __name__ == "__main__":
    tmp = Solution()
    print(tmp.func("11", "1"))
