
from calendar import Calendar, TextCalendar
from datetime import date
from typing import List

from load import load_rooms

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# class Price:
# class Bathroom:
# class Bed:

class Room:
    def __init__(self, room_number, unit, bathroom, bedCount, price):
        self.room_number = room_number
        self.unit = unit
        # self.amenities =  amenities
        # self.appliances = appliances
        # self.furniture = furniture
        self.bathroom = bathroom
        self.bedCount = bedCount
        self.price = price

    def __repr__(self) -> str:
        return f"Room(room_number={self.room_number}, bathroom={self.bathroom}, bedCount={self.bedCount}, price={self.price})"

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return f"Customer(name={self.name}, phone={self.phone}, email={self.email})"

class Reservation:
    def __init__(self, customer: Customer, rooms: List[Room], start_date, end_date):
        # customer class
        self.name = customer
        self.rooms = rooms
        self.start_date = start_date
        self.end_date = end_date
    
    # print when reservation is called
    def __repr__(self) -> str:
        return f"Reservation(name={self.name}, rooms={self.rooms}, start_date={self.start_date}, end_date={self.end_date})"

    def is_room_reserved(self, rooms: List[Room]):
        # all or nothing
        return any(room in self.rooms for room in rooms)
    


class UniversalCalendar(metaclass=Singleton):
    def __init__(self):
        self.calendar = Calendar()
        self.reservations = []
        self.total_rooms = 20

    def add_reservation(self, name, rooms: List[Room], start_date: date, end_date: date):
        # unpack start_date into start_year start_month and start_day
        start_year, start_month, start_day = start_date.year, start_date.month, start_date.day
        end_year, end_month, end_day = end_date.year, end_date.month, end_date.day
        start_date = date(start_year, start_month, start_day)
        end_date = date(end_year, end_month, end_day)
        if self.is_room_available(rooms, start_date, end_date):
            print('Reservation success')
            self.reservations.append(Reservation(name, rooms, start_date, end_date))
            return True
        print('Reservation failed')
        return False
    


    def is_room_available(self, room_numbers, start_date, end_date):
        for reservation in self.reservations:
            if reservation.is_room_reserved(room_numbers) and not (end_date < reservation.start_date or start_date > reservation.end_date):
                return False
        return True
    
    def get_reservations(self, year, month):
        return [reservation for reservation in self.reservations if reservation.start_date.year == year and reservation.start_date.month == month]
    
    def load_past_reservations(self, reservations_list):
        for reservation in reservations_list:
            self.add_reservation(reservation['name'], reservation['room_number'], reservation['start_date'], reservation['end_date'])

DriftTime = UniversalCalendar()


def load():
    
    # amenities = load_amenities()
    # appliances = load_appliances() 
    # bathrooms = load_bathrooms()
    # beds = load_beds()
    rooms = load_rooms()
    # reservations = load_reservations()

load()

#  add_reservation(self, name, rooms, start_date, end_date):
DriftTime.add_reservation("John Doe", [{1}], date(2021, 10, 1), date(2021, 10, 5))
DriftTime.add_reservation("John Doe", [1], date(2021, 10, 3), date(2021, 10, 4))
DriftTime.add_reservation("Jane Doe", [2], date(2021, 10, 6), date(2021, 10, 10))

# Load past reservations
past_reservations = [
    {"name": "John Doe", "room_number": 1, "start_date": date(2021, 10, 1), "end_date": date(2021, 10, 5)},
    {"name": "Jane Doe", "room_number": 2, "start_date": date(2021, 10, 6), "end_date": date(2021, 10, 10)}
]


# Check room availability

# print("Room 1 available from 2021-06-15 to 2021-06-20:", DriftTime.is_room_available(1, date(2021, 6, 15), date(2021, 6, 20)))

# Print reservations for June 2021
reservations = DriftTime.get_reservations(2021, 10)
print("Reservations in June 2021:", reservations.rooms[0])
exit()

# Use TextCalendar for formatted output
DriftCal = TextCalendar()
print(DriftCal.formatmonth(2021, 6))

# Print all reservations
print("All reservations:", DriftTime.reservations)
