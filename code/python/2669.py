# https://leetcode.com/problems/modify-graph-edge-weights/
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra() -> int:
            min_distance = [INF] * len(graph)
            min_distance[source] = 0
            min_heap = [(0, source)]

            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d > min_distance[u]: continue
                for v, w in graph[u]:
                    if d + w < min_distance[v]:
                        min_distance[v] = d + w
                        heapq.heappush(min_heap, (min_distance[v], v))
            return min_distance[destination]
        
        INF = int(2e9)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))
        current_shortest_distance = dijkstra()
        if current_shortest_distance < target: return []
        if current_shortest_distance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1: continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            new_distance = dijkstra()
            if new_distance <= target:
                edges[i][2] += target - new_distance
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []
