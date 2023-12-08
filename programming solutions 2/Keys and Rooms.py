class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph=defaultdict(list)

        x=0
        for room in rooms:
            graph[x]=room
            x+=1

        def bfs(node):
            queue=deque()
            queue.append(node)
            visited=set()

            while queue:
                curr=queue.popleft()
                visited.add(curr)

                for key in graph[curr]:
                    if key not in visited:
                        queue.append(key)
            
            return visited==set(list(graph))

        return bfs(0)
        
        print(graph)
        
