from collections import deque
import test

def bfs(graph, start, search):
  queue = deque()
  visited = set()
  queue += start

  while queue:
    vertice = queue.popleft()
    if vertice not in visited:
      visited.add(vertice)

      if vertice == search:
        return visited 
      else:
        diff = graph[vertice] - visited
        print "Adding to queue: {}".format(diff)
        queue += diff
        
    print "Queue: {}".format(queue)

#        A
#      /  \
#     B    C
#    / \    \
#   D   E -- F
#  /        / \  
# I ------ G   H
#
graph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A', 'F']),
  'D': set(['B', 'I']),
  'E': set(['B', 'F']),
  'F': set(['C', 'E', 'G', 'H']),
  'G': set(['I', 'F']),
  'H': set(['F']),
  'I': set(['D', 'G'])
}

print bfs(graph, 'A', 'D')