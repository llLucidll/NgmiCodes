class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_number = bin(n)
        binary_number = str(binary_number)[2:]
        for i in range(1, len(binary_number)):
            if binary_number[i] == binary_number[i - 1]:
                return False
        
        return True