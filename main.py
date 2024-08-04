
from calendar import Calendar, TextCalendar
from datetime import date

class Singleton:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Reservation:
    def __init__(self, name, room_number, start_date, end_date):
        # customer class
        self.name = name
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date
    def __repr__(self) -> str:
        return f"Reservation(name={self.name}, room_number={self.room_number}, start_date={self.start_date}, end_date={self.end_date})"


class UniversalCalendar(metaclass=Singleton):
    def __init__(self):
        self.calendar = Calendar()
        self.reservations = []
        self.total_rooms = 20

    def add_reservation(self, name, room_number, start_date, end_date):
        start_date = date(start_year, start_month, start_day)
        end_date = date(end_year, end_month, end_day)
        if self.is_room_available(room_number, start_date, end_date):
            self.reservations.append(Reservation(name, room_number, start_date, end_date))
            return True
        return False

    def is_room_available(self, room_number, start_date, end_date):
        for reservation in self.reservations:
            if reservation.room_number == room_number and not (end_date < reservation.start_date or start_date > reservation.end_date):
                return False
        return True
    
    def get_reservations(self, year, month):
        return [reservation for reservation in self.reservations if reservation.start_date.year == year and reservation.start_date.month == month]
    
    def load_past_reservations(self, reservations_list):
        for reservation in reservations_list:
            self.add_reservation(reservation['name'], reservation['room_number'], reservation['start_date'], reservation['end_date'])



DriftTime = UniversalCalendar()

# add reservation
DriftTime.add_reservation("John Doe", 1, 2021, 10, 1, 2021, 10, 5)
DriftTime.add_reservation("Jane Doe", 2, 2021, 10, 6, 2021, 10, 10)

# Load past reservations
past_reservations = [
    {"name": "John Doe", "room_number": 1, "start_date": date(2021, 10, 1), "end_date": date(2021, 10, 5)},
    {"name": "Jane Doe", "room_number": 2, "start_date": date(2021, 10, 6), "end_date": date(2021, 10, 10)}
]


# Check room availability
print("Room 1 available from 2021-06-15 to 2021-06-20:", DriftTime.is_room_available(1, date(2021, 6, 15), date(2021, 6, 20)))

# Print reservations for June 2021
reservations = DriftTime.get_reservations(2021, 6)
print("Reservations in June 2021:", reservations)

# Use TextCalendar for formatted output
DriftCal = TextCalendar()
print(DriftCal.formatmonth(2021, 6))

# Print all reservations
print("All reservations:", DriftTime.reservations)
