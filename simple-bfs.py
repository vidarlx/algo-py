from collections import deque
import unittest

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
        #print "Adding to queue: {}".format(diff)
        queue += diff
        
    #print "Queue: {}".format(queue)

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

class TestSimpleBFS(unittest.TestCase):
  def test_VerticesSearch(self):
    self.assertSetEqual(bfs(graph, 'A', 'B'), set(['A', 'B', 'C']))
    self.assertSetEqual(bfs(graph, 'A', 'D', ), set(['A', 'B', 'C', 'D', 'E', 'F']))
    self.assertSetEqual(bfs(graph, 'A', 'I', ), set(['A', 'B', 'C', 'D', 'E', 'F' ,'G', 'H', 'I']))
    self.assertSetEqual(bfs(graph, 'A', 'F', ), set(['A', 'B', 'C', 'F']))
    self.assertSetEqual(bfs(graph, 'A', 'H', ), set(['A', 'B', 'C', 'D', 'E', 'F', 'H']))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleBFS)
    unittest.TextTestRunner(verbosity=0).run(suite)