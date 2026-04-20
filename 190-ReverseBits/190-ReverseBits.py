# Last updated: 4/19/2026, 11:23:29 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        print(f"Number is: {n}")

        size = len("00000010100101000001111010011100")
        
        binary = bin(n)[2:]
        print(f"Binary is: {binary}")

        bin_size = len(binary)
        
        reversed_binary = binary[::-1] + "0" * (size - bin_size)
        print(f"Reversed binary is: {reversed_binary}")
        
        return int(reversed_binary, 2) 