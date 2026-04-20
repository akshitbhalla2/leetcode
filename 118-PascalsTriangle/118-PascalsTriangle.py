# Last updated: 4/19/2026, 11:23:43 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows <= 2:
            return [[1] * n for n in range(1, numRows+1)]

        results = [
            [1],
            [1, 1]
        ]

        for i in range(2, numRows):

            prevList = results[-1]
            tempList = [1]
            
            for j in range(i-1):
                val = prevList[j] + prevList[j+1]       
                tempList.append(val)
            
            tempList.append(1)

            results.append(tempList)

        return results


        
        

        
        