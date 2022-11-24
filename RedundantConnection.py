# given a list of edges for an undirected graph, return the last edge that can be removed such that
# the remaining edges form a tree.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = {}
        count = 1
        members = [[] for i in range(len(edges))]
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
            elif d[e[0]] != d[e[1]]:
                t = d[e[1]]
                for m in members[d[e[1]]]:
                    members[d[e[0]]].append(m)
                    d[m] = d[e[0]]
                members[t].clear()
            else:
                return e