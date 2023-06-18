def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    created_badge = []
    for name in names:
        created_badge.append(f"Hello, my name is {name}.")
    return created_badge

def assign_rooms(names):
    assigned_room = []
    for i, name in enumerate(names, start=1):
        assigned_room.append(f"Hello, {name}! You\'ll be assigned to room {i}!")
    return assigned_room

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
