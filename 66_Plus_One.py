class Solution:
    def plusOne(self, digits: list) -> list:
        """Increments the large integer by one and returns the resulting array of digits."""

        res = 0
        for i in range(len(digits)):
            res += digits[i] * (10**(len(digits)-1-i))
        res += 1

        return [int(n) for n in str(res)]


print(Solution().plusOne([4,3,2,1,]))