# Given list of dominoes laying vertically side by side, return the minimum amount of 180 degree rotations to make all tops or all bottoms the same.
# format is top[i] and bottom[i] represent the ith domino.

# idea: keep a dictionary of values, and increment when a valid value appears on top. Since it must appear on the top or bottom, there is no need to keep track of bottom as well.
# just keep the amount of dominoes as n so that you can subtract the count from it at the end in case that rotating the bottoms is faster. If a double appears, then you can decrement n
# since you obviously wouldn't need to rotate that domino.

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        d = {}
        if tops[0] == bottoms[0]: 
            d[tops[0]] = 0
            n -= 1
        else: d[tops[0]], d[bottoms[0]] = 1, 0

        for i in range(1, len(tops)):
            t, b = tops[i], bottoms[i]
            if t in d:
                if t == b:
                    n -= 1
                    self.manageDict(d, -1, t)
                    continue
                d[t] += 1
                self.manageDict(d, b, t)
                continue
            elif b in d:
                self.manageDict(d, t, b)
                continue
            return -1

        e = list(d.keys())[0]
        return d[e] if d[e] <= n/2 else n - d[e]

    def manageDict(self, d, v, keep):
        if len(d) > 1:
            if not v in d:
                for e in d:
                    if e != keep:
                        d.pop(e)
                        break