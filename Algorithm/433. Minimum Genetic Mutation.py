class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        seen = {startGene}
        while q:
            node, steps = q.popleft()
            if node == endGene:
                return steps
            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c +node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        q.append((neighbor, steps + 1))
                        seen.add(neighbor)
        return -1