class Solution:
    def romanToInt(self, s: str) -> int:
        """Converts roman numeral to integer."""

        roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }

        result = 0
        prev_value = 0

        for char in s:
            curr_value = roman_map[char]
            if curr_value > prev_value:
                result += curr_value - (2 * prev_value)
            else:
                result += curr_value
            prev_value = curr_value

        return result


print(Solution().romanToInt("XII"))