from classes.room import *
from data.save_data import rooms, save_rooms

def admin_panel():

    print("-----Admin Panel-----")
    admin = input("Enter your email or name: ")
    admin_password = input("Enter your password: ")

    if admin_password == "1234":
        print("\n-----Welcome " + admin + "-----")
        print("\n+Admin Features+")
        print("1. add new hotel rooms\n"
              "2. remove hotel rooms")

        choice = input("\nEnter your choice: ")
        if choice == "1":

            hotel_name = input("Enter hotel name: ")
            room_type = input("Enter room type: ")
            room_number = input("Enter room number: ")
            price = input("Enter price: ")

            print("\n New Room Added! \n")

            room_details = Room(hotel_name, room_number, room_type, price)
            rooms.append(room_details)
            save_rooms()

        elif choice == "2":
            found = True
            hotel_name = input("Enter hotel name: ")
            room_type = input("Enter room type: ")
            room_number = input("Enter room number: ")

            for room in rooms:
                found = True
                if ((room.room_type.lower() == room_type.lower()) and (room.room_number == room_number)) and (room.hotel_name.lower() == hotel_name.lower()):
                    found = False

                    index = rooms.index(room)
                    del rooms[index]
                    save_rooms()
                    print("***Room is removed!***")
                    break
            if found:
                print("***Reservation Not Found***")

    else:
        print("\n***Invalid  password***")
