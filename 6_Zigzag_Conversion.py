class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        from math import ceil

        # Trivial case
        if num_rows == 1:
            return s
        
        # n is number of characters
        n = len(s)
        # (2 * num_rows - 2.0) is maximum number of characters in each section
        sections = ceil(n / (2 * num_rows - 2.0))
        # (num_rows - 1) is number of columns in each section
        num_cols = sections * (num_rows - 1)
        
        # Initialize an empty 2-d array
        matrix = [[' '] * num_cols for _ in range(num_rows)]
        
        # Initialize cursors
        curr_row, curr_col = 0, 0
        curr_string_index = 0
        
        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1
            
            # Move up (with moving right also).
            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1
        
        answer = ""
        for row in matrix:
            answer += "".join(row)
            
        return answer.replace(" ", "")


print(Solution().convert("paypalishiring", 4))