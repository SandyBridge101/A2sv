class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def bfs(n):
            if n in deadends:
                return -1
            if n==target:
                print('af')
                return 0
            queue=deque()
            l=0
            queue.append([n,l])
            visited=set()
            visited.add(n)
            
            while queue:
                curr=queue.popleft()
                node,level=curr[0],curr[1]
                new_level=level+1
                #print('-->',node,level,node in visited)
                for i in range(4):
                    for dir in [1,-1]:
                        new=node[:i]+str((int(node[i])+dir)%10)+node[i+1:]
                        if new==target:
                            return new_level
                        if (new not in visited) and (new not in deadends):
                            visited.add(new)
                            queue.append([new,new_level])
            return -1
        return bfs("0000")
