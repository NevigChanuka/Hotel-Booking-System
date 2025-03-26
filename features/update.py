from data.save_data import *
from classes.booking import Booking
from classes.customer import Customer
from features.get_details import is_available, get_details

def update_reservations():
    if reservations:
        existing_customer_name = input("Enter customer name: ")
        existing_hotel_name = input("Enter hotel name: ")
        existing_room_number = input("Enter room number: ")

        found_reservation = True
        for reservation in reservations:

            if ((reservation.customer_name.lower() == existing_customer_name.lower()) and (reservation.room_number == existing_room_number)) and (reservation.hotel_name.lower() == existing_hotel_name.lower()):
                found_reservation = False
                print("\n++++Reservation Found++++")
                print("Please Re-enter details to Update\n")

                customer_name, room_type, hotel_name, customer_age, contact_number = get_details()

                available_rooms_indexes, check_in_date, check_out_date = is_available()

                if available_rooms_indexes:

                    found = True

                    for index in available_rooms_indexes:

                        if (rooms[index].room_type.lower() == room_type.lower()) and (rooms[index].hotel_name.lower() == hotel_name.lower()):

                            found = False
                            index = reservations.index(reservation)
                            reservations[index] = Booking(customer_name, hotel_name, room_type, rooms[index].room_number, check_in_date, check_out_date)
                            users[index] = Customer(customer_name, customer_age, contact_number, rooms[index].room_number)

                            save_reservations()
                            save_users()
                            print("***Updated Successfully!***")

                            print("***Reservations updated***")
                            break

                    if found:
                        print("***Rooms Not Available***")


                else:
                    print("***Rooms Not Available for Entered Date***")
                break

        if found_reservation:
            print("***Reservation Not Found***")

    else:
        print("***Reservation Not Found***")

