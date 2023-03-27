class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Returns the sum of two strings as a binary string."""

        res = ""
        carry = 0

        # Reverse order for addition
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            total = digitA + digitB + carry
            
            # char = 0/2 [add "0" to res]
            # char = 1/3 [add "1" to res]
            char = str(total % 2)
            res += char

            # total = 2/3 [update carry to "1"]
            carry = total // 2
        
        # Check final case of carry = 1
        if carry:
            res += "1"

        return res[::-1]

        
print(Solution().addBinary("1010", "1011"))