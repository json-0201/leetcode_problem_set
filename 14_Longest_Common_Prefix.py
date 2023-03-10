class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """Returns the longest prefix string from an array of strings"""

        prefix = ""
        n = min([len(s) for s in strs])

        for i in range(n):
            char = [s[i] for s in strs]

            if len(set(char)) == 1:
                prefix += strs[0][i]
            else:
                break

        return prefix


print(Solution().longestCommonPrefix(["cir","car"]))