# Given list of intervals(arrays of length 2 denoting start and end of interval) return a list of non-overlapping intervals (intervals are inclusive)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        o = []
        start = 0
        prev = -2
        for i in intervals:
            if i[0] <= prev:
                prev = max(prev, i[1])
            else:
                o.append([start, prev])
                start = i[0]
                prev = i[1]
        o.append([start, prev])
        return o[1:]