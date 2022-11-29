# given array, return k most common elements.
# short and sweet.

import queue as q

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if not i in d:
                d[i] = 0
            d[i] += 1

        return sorted(d.keys(), key=lambda s: d[s], reverse=True)[:k]