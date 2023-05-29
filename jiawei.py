from collections import deque

def bfs(graph, source, target, parent):
    # Perform BFS to find the augmenting path from source to target
    queue = deque([source])
    parent[source] = -1
    max_flow = float('inf')

    while queue:
        node = queue.popleft()
        for neighbor, capacity, flow in graph[node]:
            if parent[neighbor] is None and capacity > flow:
                parent[neighbor] = node
                max_flow = min(max_flow, capacity - flow)
                if neighbor == target:
                    return max_flow
                queue.append(neighbor)

    return 0

def edmonds_karp_max_flow(graph, source, target):
    # Initialize the maximum flow to 0
    max_flow = 0

    while True:
        # Create an array to store the parent nodes for each vertex in the augmenting path
        parent = [None] * len(graph)

        # Find an augmenting path using BFS and compute the bottleneck capacity
        bottleneck = bfs(graph, source, target, parent)
        if bottleneck == 0:
            break  # No more augmenting paths exist

        # Update the flow in the augmenting path and the residual capacities
        v = target
        while v != source:
            u = parent[v]
            for i, (neighbor, capacity, flow) in enumerate(graph[u]):
                if neighbor == v:
                    graph[u][i] = (neighbor, capacity, flow + bottleneck)
                    break
            for i, (neighbor, capacity, flow) in enumerate(graph[v]):
                if neighbor == u:
                    graph[v][i] = (neighbor, capacity, flow - bottleneck)
                    break
            v = u

        # Add the bottleneck capacity to the maximum flow
        max_flow += bottleneck

    return max_flow

def combine(start, finish, layout):
    temp = 0
    combined_layout = []
    storageroom = [0 for _ in range(len(layout))]

    # Combine storage rooms
    for y in range(len(layout)):
        for x in start:
            storageroom[y] += layout[x][y]

    for x in range(len(start)):
        storageroom.pop(0)
    storageroom.insert(0, 0)

    for x in range(len(finish)):
        temp = storageroom.pop() + temp
    storageroom.append(temp)

    combined_layout.append(storageroom)

    # Combine intermediate rooms
    intermediateroom = [[0 for _ in range(len(layout) - len(start) - len(finish) + 2)] for _ in range(len(layout) - len(start) - len(finish))]
    for x in range(len(intermediateroom)):
        intermediateroom[x][-1] = sum(layout[len(start) + x])
        combined_layout.append(intermediateroom[x])

    # Combine delivery rooms
    deliveryroom = [0 for _ in range(len(storageroom))]
    combined_layout.append(deliveryroom)

    return combined_layout



# Define the graph based on the combine_layout
start = [0, 1]
finish = [4, 5]
layout = [
    [0, 0, 4, 6, 0, 0],  # room 0: storage room
    [0, 0, 5, 2, 0, 0],  # room 1: storage room
    [0, 0, 0, 0, 4, 4],  # room 2: intermediate room
    [0, 0, 0, 0, 6, 6],  # room 3: intermediate room
    [0, 0, 0, 0, 0, 0],  # room 4: delivery room
    [0, 0, 0, 0, 0, 0],  # room 5: delivery room
]

combine_layout=combine(start,finish,layout)
# print(combine_layout)
num_rooms = len(combine_layout)
source = 0
target = num_rooms - 1

# Initialize the graph as an adjacency list with (neighbor, capacity, flow) tuples
graph = [[] for _ in range(num_rooms)]

# Build the graph edges/capacities based on the combine_layout
for i in range(num_rooms):
    for j in range(num_rooms):
        capacity = combine_layout[i][j]
        if capacity > 0:
            # Add forward edge from i to j
            graph[i].append((j, capacity, 0))
            # Add backward edge from j to i (capacity is 0 for the backward edge)
            graph[j].append((i, 0, 0))

# Compute the maximum flow using Edmonds-Karp algorithm
max_flow = edmonds_karp_max_flow(graph, source, target)

print(max_flow)
# print("combine_layout lens", len(layout))
# print("start lens",len(start))
# print("finish lens",len(finish))
