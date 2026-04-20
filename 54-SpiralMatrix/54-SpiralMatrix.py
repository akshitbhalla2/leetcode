# Last updated: 4/19/2026, 11:23:57 PM
import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        k = min(m, n) 

        if k != 1:
            k = math.ceil(k/2)
            # if k % 2 == 0:
            #     k = k // 2
            # else:
            #     k = k // 2 + 1

        def getCoordinates(topLeft):

            coordinates = [topLeft]

            i, j = topLeft
            topRight = (i, n-1-j)
            bottomRight = (m-1-i, n-1-j)
            bottomLeft = (m-1-i, j)

            if topLeft == topRight:
                # Vertical line
                if topLeft[0] < bottomLeft[0]:
                    coordinates.append(bottomLeft)
                return coordinates

            if topLeft == bottomLeft:
                # Horizontal line
                if topLeft[1] < topRight[1]:
                    coordinates.append(topRight)
                return coordinates

            # Rectangle
            coordinates.extend([topRight, bottomRight, bottomLeft])
            return coordinates

        results = []
        for i in range(k):
            
            results.append((i, i))
            coordinates = getCoordinates((i, i))

            size = len(coordinates)

            if size == 4:
                topLeft, topRight, bottomRight, bottomLeft = coordinates

                for j in range(topLeft[1]+1, topRight[1]+1):
                    results.append((topLeft[0], j))

                for i in range(topRight[0]+1, bottomRight[0]+1):
                    results.append((i, topRight[1]))

                for j in range(bottomRight[1]-1, bottomLeft[1]-1, -1):
                    results.append((bottomRight[0], j))

                for i in range(bottomLeft[0]-1, topLeft[0], -1):
                    results.append((i, bottomLeft[1]))

            elif size == 2:
                A, B = coordinates

                # A (1, 1) and B (9, 1)
                # A (1, 1) and B (1, 9)

                if A[1] < B[1]:
                    for j in range(A[1]+1, B[1]+1):
                        results.append((A[0], j))
                
                else:
                    for i in range(A[0]+1, B[0]+1):
                        results.append((i, A[1]))

        temp = []
        for res in results:
            x, y = res
            temp.append(matrix[x][y])

        return temp
            


            








