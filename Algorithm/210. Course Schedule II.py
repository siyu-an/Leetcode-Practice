#Topological sort: Kahn's Algorithm
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        ind = [0] * numCourses
        for pairs in prerequisites:
            pre = pairs[1]
            post = pairs[0]
            adj[pre].append(post)
            ind[post] += 1
        q = deque()
        order = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            for p in adj[curr]:
                ind[p] -= 1
                if ind[p] == 0:
                    q.append(p)
            order.append(curr)
        return order if len(order) == numCourses else []
