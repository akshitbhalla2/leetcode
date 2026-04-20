# Last updated: 4/19/2026, 11:23:09 PM
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        size = len(s)

        left = 0
        right = 0
        
        result = 0
        # max_freq = 0  

        count = Counter()

        while right < size:

            char = s[right] 
            count[char] += 1

            max_freq = max(count.values())
            # max_freq = max(max_freq, count[char])
            
            window_size = right - left + 1
            num_updates = window_size - max_freq

            if num_updates <= k:
                result = max(result, window_size)
            else:
                char = s[left]
                count[char] -= 1
                left += 1

            right += 1

        return result