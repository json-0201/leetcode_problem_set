class Solution:
    def myAtoi(self, s: str) -> int:
        import re

        # Remove leading whitespaces
        s = s.lstrip()
        
        # Empty string / Non-digit single character
        if not s or (len(s) == 1 and not s.isdigit()):
            return 0

        # Detect negative sign
        if s[0] == "-":
            negative = True
        # Detect positive sign
        elif s[0] == "+":
            s = s[1:]
            negative = False
        # No sign => positive integer
        else:
            negative = False

        # If digit does not come after sign
        if not negative and not s[0].isdigit():
            return 0
        if negative and not s[1].isdigit():
            return 0

        # Detect digits
        regex = "\d+"
        num = re.findall(regex, s)[0]

        if negative:
            num = int(num) * -1
        else:
            num = int(num)

        # Limit integer
        if num < -2**31:
            num = -2**31
        if num > 2**31 - 1:
            num = 2**31 -1

        return num


print(Solution().myAtoi("4193 with words"))