# Last updated: 4/19/2026, 11:23:59 PM
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        visited = {}
        results = []
        index = 0

        for str_ in strs:
            
            sorted_str = sorted(str_)
            sorted_str = "".join(sorted_str)

            if sorted_str in visited:
                i = visited[sorted_str]
                results[i] = results[i] + [str_]
            
            else:
                visited[sorted_str] = index
                results.append([str_])
                index += 1

        return results
            











