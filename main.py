from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  """
  Params: 
    graph.....a graph represented as a dict where each key is a vertex
              and the value is a set of (vertex, weight) tuples (as in the test case)
    source....the source node
    
  Returns:
    a dict where each key is a vertex and the value is a tuple of
    (shortest path weight, shortest path number of edges). See test case for example.
  """
  visited = {}
  frontier = []
  heappush(frontier, (0, 0, source))  # Flatten the tuple structure

  while frontier:
      distance, edges, node = heappop(frontier)

      if node not in visited or (distance < visited[node][0]):
          visited[node] = (distance, edges)

          for neighbor, weight in graph[node]:
              if neighbor not in visited:
                  heappush(frontier, (distance + weight, edges + 1, neighbor))

  return visited


def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    visited = set()
    frontier = deque()
    frontier.append(source)
    parentset = {source: None}
  
    while frontier:
        node = frontier.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parentset[neighbor] = node
                frontier.append(neighbor)
    return parentset
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    current  = parents[destination]
    while current:
      path.append(current)
      current = parents[current]
    return ''.join(path[::-1])

