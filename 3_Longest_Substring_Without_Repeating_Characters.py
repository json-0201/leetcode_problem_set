class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.
        String s consists of English letters, digits, symbols and spaces.
        """

        # trivial input
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        temp, words = [], []
        index = 0

        while s:
            if index == len(s):
                words.append("".join(temp))
                break
            elif s[index] in temp:
                words.append("".join(temp))
                temp = []
                s = "".join([char for char in s][1:])
                index = 0
            temp.append(s[index])
            index += 1
            
        return len(max(words, key=len))

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
