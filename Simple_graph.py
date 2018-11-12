graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']
         }

def breadth_first_search(graph, start_vertex):
    visited, verticies = [], [start_vertex]
    if graph and start_vertex and start_vertex in graph:
        while verticies:
            vertex = verticies.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                verticies.extend ([v for v in graph[vertex] if v not in visited] )
    return visited

print(breadth_first_search(graph, 'A'))

while True:
    start_vertex = input("Please input start vertex:")
    if start_vertex:
        print(breadth_first_search(graph, start_vertex))
    else: break



