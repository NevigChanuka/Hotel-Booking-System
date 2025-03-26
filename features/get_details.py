import datetime
from data.save_data import *
from classes.booking import Booking
from classes.customer import Customer
from features.generate_receipt import generate_receipt


# checks the room is available
def is_available():

    global check_in_date, check_out_date

    is_date_correct = True

    # getting date and validating
    while is_date_correct:

        try:
            check_in_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").date()  # get check in date
            check_out_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").date()   # get check out date

            if not ((datetime.date.today() <= check_in_date) and (check_in_date <= check_out_date)):
                 raise ValueError

            else:
                is_date_correct = False

        except ValueError:
            print("\n****Invalid date****"
                  "\nPlease Re-enter the Date\n")


    available_rooms_indexes = []

    for room in rooms:
        available_rooms_indexes.append(rooms.index(room))


    # only execute when reservations have elements
    if reservations:

        for reservation in reservations:
            if not ((reservation.check_out_date < check_in_date) or (reservation.check_in_date > check_out_date)):

                for room in rooms:
                    if (room.room_type.lower() == reservation.room_type.lower() and (room.room_number == reservation.room_number)) and (room.hotel_name.lower() == reservation.hotel_name.lower()):
                        available_rooms_indexes.remove(rooms.index(room))
                        #print(rooms.index(room))

    #print(available_rooms_indexes)
    return available_rooms_indexes, check_in_date, check_out_date





def get_details():

    if rooms:
        customer_name = input("Enter your name: ")
        customer_age = input("Enter your age: ")
        contact_number = input("Enter contact number: ")
        hotel_name = input("Enter hotel name: ")

        while True:
            print("\n+++Select your room++++\n")

            print("1. Single Room $30")
            print("2. Double Room $50")
            print("3. Family Room $150")

            room_types = input("Enter your choice: ")

            if room_types == "1":
                room_type = "single"
                break
            elif room_types == "2":
                room_type = "double"
                break
            elif room_types == "3":
                room_type = "family"
                break
            else:
                print("***Invalid choice***")

    else:
        print("\n***No rooms available***")

    return customer_name, room_type, hotel_name, customer_age, contact_number





def booking():

    customer_name, room_type, hotel_name, customer_age, contact_number = get_details()

    available_rooms_indexes, check_in_date, check_out_date = is_available()

    available = True

    if available_rooms_indexes:

        for index in available_rooms_indexes:
            if (rooms[index].room_type.lower() == room_type.lower()) and (
                    rooms[index].hotel_name.lower() == hotel_name.lower()):
                available = False

                booking_details = Booking(customer_name, hotel_name, room_type, rooms[index].room_number, check_in_date,
                                          check_out_date)
                reservations.append(booking_details)
                save_reservations()

                print("\nRoom Booked Successfully")
                print("Your Room Number is: " + rooms[index].room_number)
                generate_receipt(customer_name, customer_age, contact_number, hotel_name, room_type,
                                 rooms[index].room_number, check_in_date, check_out_date)

                customer_details = Customer(customer_name, customer_age, contact_number, rooms[index].room_number)
                users.append(customer_details)
                save_users()

                break

    else:
        print("\n***No rooms available***")

    if available:
        print("\n***No rooms available***")



