import datetime
from data.save_data import users,rooms,reservations
from classes.customer import Customer
from classes.room import Room
from classes.booking import Booking



# load user data from text file
def load_users():
    try:
        with open("data/Customers", 'r') as file:
            for line in file:
                customer_name, customer_age, contact_number, room_number = line.strip().split(',')
                users.append(Customer(customer_name, customer_age, contact_number, room_number))
    except (FileNotFoundError, ValueError):
        pass


# load room data from text file
def load_rooms():
    try:
        with open("data/Hotel Rooms", 'r') as file:
            for line in file:
                hotel_name, room_number, room_type, price = line.strip().split(',')
                rooms.append(Room(hotel_name, room_number, room_type, price))
    except (FileNotFoundError, ValueError):
        pass


# load reservation data from text file
def load_reservations():
    try:
        with open("data/Hotel Reservations", 'r') as file:
            for line in file:
                customer_name, hotel_name, room_type, room_number, check_in_date, check_out_date = line.strip().split(',')
                reservations.append(Booking(customer_name,
                                            hotel_name,
                                            room_type,
                                            room_number,
                                            datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date(),
                                            datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()))
    except (FileNotFoundError, ValueError):
        pass
