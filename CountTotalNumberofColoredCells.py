# https://leetcode.com/problems/count-total-number-of-colored-cells/description/

class Solution:
    def coloredCells(self, n: int) -> int:
        edge = max(0, n - 2)
        corner = n-1
        
        out = 1
        if edge: edge = edge*(edge + 1)/2
        edge *= 4
        corner *= 4

        return int(out + edge + corner)