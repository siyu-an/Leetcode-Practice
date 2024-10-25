#Topological ordering: Kahn's Algorithm
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        ans = []
        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            adj[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            current = queue.popleft()
            ans.append(current)
            for course in adj[current]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return len(ans) == numCourses
        