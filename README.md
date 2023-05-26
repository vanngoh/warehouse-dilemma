# Warehouse Dilemma
> This repository is just for education purpose

### Description

Your task is to design an algorithm to efficiently transport parcels from different rooms in a warehouse to the delivery sections. The warehouse is divided into interconnected rooms, each with a specific limit on the number of parcels that can be carried through its doors at one time.

You are given as inputs a list of room numbers start, representing the rooms from which the parcels need to be retrieved, a list of room numbers finish, representing the rooms where the parcels will be picked up for delivery, and a matrix layout that indicates the maximum number of parcels that can be transported at once between each pair of rooms, where layout[i][j] = x means that up to x parcels can be transported from room i to room j at a time. It is guaranteed that the start rooms and the finish rooms do not intersect.

Write an algorithm in Python that computes the maximum number of parcels that can be transported at a time.

### Example 1
Input:
```
start = [0, 1]
finish = [4, 5]
layout = [
    [0, 0, 4, 6, 0, 0],  # room 0: storage room
    [0, 0, 5, 2, 0, 0],  # room 1: storage room
    [0, 0, 0, 0, 4, 4],  # room 2: intermediate room
    [0, 0, 0, 0, 6, 6],  # room 3: intermediate room
    [0, 0, 0, 0, 0, 0],  # room 4: delivery room
    [0, 0, 0, 0, 0, 0],  # room 5: delviery room
]
```
Output:
```
16
```
In each time step, the following might happen:
- From room 0, send 4/4 parcels to room 2, and 6/6 parcels to room 3
- From room 1, send 4/5 parcels to room 2, and 2/2 parcels to room 3
- From room 2, send 4/4 parcels to room 4, and 4/4 parcels to room 5
- From room 3, send 4/6 parcels to room 4, and 4/6 parcels to room 5


So, 16 parcels can be transported to the delivery stations at rooms 4 and 5 at each time step.

### Constraints

len(layout) <= 100

layout[i][j] <= 1000000
