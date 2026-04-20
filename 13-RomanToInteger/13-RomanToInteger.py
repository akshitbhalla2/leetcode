# Last updated: 4/19/2026, 11:24:09 PM
class Solution:
    def romanToInt(self, s: str) -> int:

        rom_to_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integers = []
        n = 0
        for char in s:
            integers.append(rom_to_int_map[char])
            n += 1
        
        total = 0
        for i in range(0, n-1):
            if integers[i] < integers[i+1]:
                integers[i] *= -1
            total += integers[i]
        total +=  integers[-1]

        return total