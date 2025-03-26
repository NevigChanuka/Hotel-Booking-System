reservations = []
rooms = []
users = []

# save user data to text file
def save_users():
    with open("data/Customers", 'w') as file:
        for user in users:
            file.write(f"{user.customer_name},{user.customer_age},{user.contact_number},{user.room_number}\n")




# save room data to text file
def save_rooms():
    with open("data/Hotel Rooms", 'w') as file:
        for room in rooms:
            file.write(f"{room.hotel_name},{room.room_number},{room.room_type},{room.price}\n")




# save reservation data to text file
def save_reservations():
    with open("data/Hotel Reservations", 'w') as file:
        for reservation in reservations:
            file.write(f"{reservation.customer_name},"
                       f"{reservation.hotel_name},"
                       f"{reservation.room_type},"
                       f"{reservation.room_number},"
                       f"{reservation.check_in_date },"
                       f"{reservation.check_out_date}\n")


