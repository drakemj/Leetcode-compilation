# https://leetcode.com/problems/frog-position-after-t-seconds/description/

class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        if target == 1:
            if not len(edges): return 1.0
            else: return 0.0
        d = defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        p = self.dfs(1, d, [], [], target)
        total = 1.0/len(d[1])

        for e in p[1:-1]:
            total/=(len(d[e]) - 1)
        if t+1 == len(p) or t+1 > len(p) and len(d[p[-1]]) == 1:
            return total
        else: return 0

    def dfs(self, n, d, seen, path, target):
        seen.append(n)
        path.append(n)
        if n == target: return path
        for e in d[n]:
            if e not in seen:
                r = self.dfs(e, d, seen, path, target)
                if r: return r
                path.pop()
        return None