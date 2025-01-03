class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        def build_graph(equations, values):
            def add_edges(f, t, value):
                if f in graph:
                    graph[f].append((t,value))
                else:
                    graph[f] = [(t, value)]
            for v, value in zip(equations, values):
                f, t = v
                add_edges(f, t, value)
                add_edges(t, f, 1/value)
        def find_path(query):
            b, e = query
            if b not in graph or e not in graph:
                return -1.0
            q = deque([(b, 1.0)])
            visited = set()
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product * value))
            return -1.0
        build_graph(equations, values)
        return[find_path(q) for q in queries]