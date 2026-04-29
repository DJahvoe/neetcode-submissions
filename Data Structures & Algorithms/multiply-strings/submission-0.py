class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle zero shortcut early
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse strings to simplify multiplication from least significant digit
        a = num1[::-1]
        b = num2[::-1]

        # Result array (max possible digits = len(a) + len(b))
        result = [0] * (len(a) + len(b))

        # Multiply each digit pair
        for i in range(len(a)):
            for j in range(len(b)):
                product = int(a[i]) * int(b[j])
                result[i + j] += product

                # Handle carry immediately
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros from the reversed result
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert back to string
        return ''.join(map(str, result[::-1]))
