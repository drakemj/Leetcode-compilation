# given a list of edges for an undirected graph, return the last edge that can be removed such that
# the remaining edges form a tree.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = {}  # dict for to which group a node belongs to
        count = 1   # current group
        members = [[] for i in range(len(edges))]   # index i holds all members of ith group
        for e in edges:
            if not e[0] in d and not e[1] in d:
                count += 1
                for i in range(2):
                    d[e[i]] = count
                    members[count].append(e[i])
            elif not e[0] in d:
                d[e[0]] = d[e[1]]
                members[d[e[0]]].append(e[0])
            elif not e[1] in d:
                d[e[1]] = d[e[0]]
                members[d[e[0]]].append(e[1])
            elif d[e[0]] != d[e[1]]:    # merge two groups
                t = d[e[1]]
                for m in members[d[e[1]]]:
                    members[d[e[0]]].append(m)
                    d[m] = d[e[0]]
                members[t].clear()
            else:   # if connecting two nodes already connected, return this edge
                return e