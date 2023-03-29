class Solution:
    def climbStairs(self, n: int) -> int:
        """Recursive solution (fibonacci)."""

        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return b


print(Solution().climbStairs(3))