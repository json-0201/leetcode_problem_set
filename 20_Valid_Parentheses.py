class Solution:
    def isValid(self, s: str) -> bool:
        """()/{}/[] string validator"""

        stack = []
        parentheses_hash_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            # if closing side -> check for match and pop
            if char in parentheses_hash_map:
                if stack and stack[-1] == parentheses_hash_map[char]:
                    stack.pop()
                else:
                    return False
            # if open side -> append to stack
            else:
                stack.append(char)

        return True if not stack else False


print(Solution().isValid("(}{)"))