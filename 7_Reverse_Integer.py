class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0 :
            negative = True
            x *= -1

        res = ""
        for i in range(len(str(x))-1, -1, -1):
            res += str(x)[i]

        if not negative:
            res = int(res)
        else:
            res = int(res) * -1

        return res if (res > -2**31 and res < 2**31 - 1 ) else 0


print(Solution().reverse(120))