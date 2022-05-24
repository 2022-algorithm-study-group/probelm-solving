## https://leetcode.com/problems/reconstruct-itinerary/

from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            print("now : " + origin + ", " + nextDest)
            self.DFS(nextDest)
        print("append!" + origin)
        self.result.append(origin)

# print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["SFO","JFK"],["ATL","SFO"]]))