
def solution(start, finish, layout):
    total_deliverable_parcels = 0

    # Generate the first next_rooms
    # Note: start here is list type
    first_batch = generate_next_rooms(start, finish, layout, total_deliverable_parcels)
    next_rooms = first_batch[0]

    while len(next_rooms.keys()) > 0:
        # Note: next_rooms here is dict type
        result = generate_next_rooms(next_rooms, finish, layout, total_deliverable_parcels)
        
        # Check if there still have next_rooms
        if (len(result[0].keys()) > 0):
            next_rooms = result[0]
        else:
            next_rooms = {}

        # Update the total_deliverable_parcels
        total_deliverable_parcels = result[1]
    
    return total_deliverable_parcels
        

def generate_next_rooms(rooms, finish, layout, total_deliverable_parcels):
    next_rooms = {}
    for room_number in rooms:
        for (index, deliverable_parcels) in enumerate(layout[room_number]):
            if deliverable_parcels == 0:
                continue

            if index not in finish:
                if index not in next_rooms.keys():
                    next_rooms[index] = 0
                next_rooms[index] += deliverable_parcels
                continue

            # Found the delivery room, so need to do the comparison
            # to find out the bottleneck to deliver the parcel
            if deliverable_parcels < rooms[room_number]:
                rooms[room_number] -= deliverable_parcels
                total_deliverable_parcels += deliverable_parcels
            else:
                total_deliverable_parcels += rooms[room_number]
                rooms[room_number] = 0
    
    return (next_rooms, total_deliverable_parcels)


# Manual check
# start = [0, 1]
# finish = [4, 5]
# layout = [
#     [0, 0, 4, 6, 0, 0],
#     [0, 0, 5, 0, 0, 0],
#     [0, 0, 0, 3, 4, 0],
#     [0, 0, 0, 0, 0, 6],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
# ]
# start = [0]
# finish = [3]
# layout = [
#     [0, 7, 0, 0],
#     [0, 0, 6, 0],
#     [0, 0, 0, 8],
#     [9, 0, 0, 0]
# ]
# solution(start, finish, layout)


if __name__ == "__main__":
    assert solution(
        [0, 1],
        [4, 5],
        [
            [0, 0, 4, 6, 0, 0],
            [0, 0, 5, 2, 0, 0],
            [0, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 6, 6],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    ) == 16

    assert solution(
        [0],
        [3],
        [
            [0, 7, 0, 0],
            [0, 0, 6, 0],
            [0, 0, 0, 8],
            [9, 0, 0, 0]
        ]
    ) == 6

    assert solution(
        [0, 1],
        [4, 5],
        [
            [0, 0, 4, 6, 0, 0],
            [0, 0, 5, 0, 0, 0],
            [0, 0, 0, 3, 4, 0],
            [0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ) == 13

    assert solution(
        [0, 1],
        [4, 5],
        [
            [0, 0, 4, 6, 0, 0],
            [0, 0, 5, 2, 0, 0],
            [0, 0, 0, 0, 4, 6],
            [0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ) == 15

    assert solution(
        [0],
        [5],
        [
            [0, 10, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0],
            [0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    ) == 1

    
    print("All tests passed!")
