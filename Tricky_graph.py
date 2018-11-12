

def breadth_first_search(graph, start_vertex):

    visited, verticies = [], [start_vertex]
    if graph and start_vertex and start_vertex in graph:
        while verticies:
            vertex = verticies.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                verticies.extend ([v for v in graph[vertex] if v not in visited] )
    return visited

def add_graph_vertex(graph, vertex, edges):
    if not edges:
        graph[vertex]=[]
        edges = edges.split(',')
        if vertex in graph:
            for edge in edges:
                if edge not in graph[vertex]:
                    graph[vertex].append(edge)
                else:
                    graph[vertex] = edges
                for edge in edges:
                    if edge in graph:
                        graph[edge].append(vertex)
                    else:
                        graph[edge]= [vertex]

graph = {}

while True:
    vertex = input("Please input start vertex:")
    if not vertex:
        continue

        edges = input(f"Please input edges separated by ','for {vertex}: ")
        add_graph_vertex(graph, vertex, edges)
        print(graph)
        next_vertex = input("Stop Adding verticies(y/yes)", "Press enter to continue:")
        if next_vertex.lower() in ('y', 'yes'):
            break
while True:
    start_vertex = input("Please input start vertex:")
    if start_vertex:
        print(breadth_first_search(graph, start_vertex))
    else: break
