from main import Room

def load_rooms():
    
# loadrooms into the system
# room_number, unit, bathroom, bedCount, price
    rooms = [
        Room(1, "A", 0, 100),
        Room(2, "A", 1, 100),
        Room(3, "A", 0, 100),
        Room(4, "A", 1, 100),
        Room(5, "A", 0, 100),
        Room(6, "A", 1, 100),
        Room(7, "A", 0, 100),
        Room(8, "B", 0, 100),
        Room(9, "B", 1, 100),
        Room(10, "B", 0, 100),
        Room(11, "B", 1, 100),
        Room(12, "B", 0, 100),
        Room(13, "B", 1, 100),
        Room(14, "B", 0, 100),
        Room(15, "C", 0, 100),
        Room(16, "C", 1, 100),
        Room(17, "C", 0, 100),
        Room(18, "C", 1, 100),
        Room(19, "C", 0, 100),
        Room(20, "C", 1, 100)
    ]
    return rooms