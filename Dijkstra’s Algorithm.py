# Dijkstra's Algorithm in Python
import sys

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]


# Find which vertex is to be visited next
def vertex_to_be_visited():
    global distance_and_visited
    v = -10
    for index in range(numofvertices):
        if distance_and_visited[index][0] == 0 \
                and (v < 0 or distance_and_visited[index][1] <=
                     distance_and_visited[v][1]):
            v = index
    return v


numofvertices = len(vertices[0])

distance_and_visited = [[0, 0]]
for i in range(numofvertices - 1):
    distance_and_visited.append([0, sys.maxsize])

for vertex in range(numofvertices):

    # Find next vertex to be visited
    to_visit = vertex_to_be_visited()
    for neighborindex in range(numofvertices):

        # Updating new distances
        if vertices[to_visit][neighborindex] == 1 and \
                distance_and_visited[neighborindex][0] == 0:
            new_distance = distance_and_visited[to_visit][1] \
                           + edges[to_visit][neighborindex]
            if distance_and_visited[neighborindex][1] > new_distance:
                distance_and_visited[neighborindex][1] = new_distance

        distance_and_visited[to_visit][0] = 1

i = 0

# Printing the distance
for distance in distance_and_visited:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1
