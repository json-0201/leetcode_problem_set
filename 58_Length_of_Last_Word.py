class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Returns the length of the last word in the string."""

        return len(s.split()[-1])


print(Solution().lengthOfLastWord("Hello World"))