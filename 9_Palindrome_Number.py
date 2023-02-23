class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative integer
        if x < 0:
            return False

        # Iterate in pairs
        for i in range(len(str(x)) // 2):
            if str(x)[i] != str(x)[len(str(x))-1-i]:
                return False

        return True

print(Solution().isPalindrome(10))