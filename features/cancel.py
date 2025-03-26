from data.save_data import *

def cancel_reservations():
    if reservations:
        found = True

        customer_name = input("Enter customer name: ")
        hotel_name = input("Enter hotel name: ")
        room_number = input("Enter room number: ")


        for reservation in reservations:

            if ((reservation.customer_name.lower() == customer_name.lower()) and (reservation.room_number == room_number)) and (reservation.hotel_name.lower() == hotel_name.lower()):
                found = False
                index = reservations.index(reservation)

                del reservations[index]
                del users[index]

                save_reservations()
                save_users()
                print("***Reservation canceled!***")
                break

        if found:
            print("***No Reservations***")

    else:
        print("***No Reservations***")
