# Given undirected graph, count all pairs of unconnected nodes.

class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        groupNum = 0
        group = {}
        members = {}
        
        for e in edges:
            if not e[0] in group and not e[1] in group:
                groupNum += 1
                group[e[0]] = group[e[1]] = groupNum
                members[groupNum] = [e[0], e[1]]
            elif not e[0] in group:
                g = group[e[1]]
                group[e[0]] = g
                members[g].append(e[0])
            elif not e[1] in group:
                g = group[e[0]]
                group[e[1]] = g
                members[g].append(e[1])
            elif group[e[0]] != group[e[1]]:
                g = group[e[0]]
                old = group[e[1]]
                for m in members[old]:
                    group[m] = g
                    members[g].append(m)
                del members[old][:]
        
        pool = []
        for m in members:
            l = len(members[m])
            if l: pool.append(l)

        out = 0
        for e in pool:
            n -= e
            out += e*n
        if n:
            out += n*(n-1)/2
        return out