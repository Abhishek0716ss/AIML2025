from collections import deque
graph={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dfs_using_stack(graph, start):
    stack = [start]
    visited=set()
    while stack:
        current_node=stack.pop()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            for neighbour in graph[current_node]:
              stack.append(neighbour)
            
dfs_using_stack(graph, 'A')
