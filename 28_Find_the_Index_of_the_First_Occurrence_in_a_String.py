class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Returns the index of the first occurrence in a string."""
        
        for i in range(len(haystack)):
            s = haystack[i:]
            if s[:len(needle)] == needle:
                return i
        
        return -1


print(Solution().strStr("leetcode", "leeto"))