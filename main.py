from data.load_data import *
from data.save_data import *
from features.filters import search_rooms
from features.update import update_reservations
from features.cancel import cancel_reservations
from features.admin import admin_panel
from features.view_available_rooms import view_available_rooms
from features.get_details import booking



def main():
    load_rooms()
    load_reservations()
    load_users()

    print("-----------Hotel Rooms-----------")
    for room in rooms:
        print(f"Hotel - {room.hotel_name} | Room Number - {room.room_number} | Room Type - {room.room_type} | Price - {room.price}")

    while True:

        print("\n--- Hotel Room Booking System ---")
        print("1. Search Rooms")
        print("2. View available rooms")
        print("3. Book a room")
        print("4. Update reservation")
        print("5. Cancel reservation")
        print("6. Hotel admin")
        print("7. Exit")
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
           search_rooms()

        elif choice == "2":
            view_available_rooms()

        elif choice == "3":
            booking()

        elif choice == "4":
            update_reservations()

        elif choice == "5":
            cancel_reservations()

        elif choice == "6":
            admin_panel()

        elif choice == "7":
            break

        else:
            print("\nInvalid choice")



if __name__ == '__main__':
    main()


