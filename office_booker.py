class Offices:
    """
    This is a python class for office management.
    To initiate it give it a list of the available rooms
    offices  = Offices([room1,room2,room3])

    In the beginning all the rooms are available all the time
    """

    rooms = {}

    def __init__(self, rooms) -> None:
        for i in rooms:
            self.rooms[i] = []

    def book_room(self,room_number, time):
        self.rooms[room_number].append(time)

    def room_availibility(self,room, time):
        if time in self.rooms[room]:
            return f"Room {room} is booked from {time} to {time+1}"
        else:
            return f"Room {room} is available from {time} to {time+1}"
    
    

Offices = Offices([1,2,3,4,5])
Offices.book_room(3,2)
print(Offices.rooms)
