class Solution:
    def mySqrt(self, x: int) -> int:
        """Returns the square root of x rounded down to the nearest integer."""

        return int(x ** (1/2))


print(Solution().mySqrt(8))