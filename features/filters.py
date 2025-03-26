from data.save_data import rooms
from features.get_details import is_available

# search rooms by type
def search_by_type():

    room_type = input("Enter room type(single/double/family): ")
    is_valid_room_type = True

    for room in rooms:
        if room.room_type.lower() == room_type.lower():
            print(f"Hotel - {room.hotel_name} | Room Number - {room.room_number} | Room Type - {room.room_type} | Price - {room.price}")
            is_valid_room_type = False

    if is_valid_room_type:
        print("***Room Type Is Invalid***")


# search rooms by prices
def search_by_price():
    room_price = input("Enter room price: ").replace("$", "")

    found = True

    for room in rooms:

        if int(room.price.replace("$", "")) <= int(room_price):
            found = False
            print(f"Hotel - {room.hotel_name} | Room Number - {room.room_number} | Room Type - {room.room_type} | Price - {room.price}")

    if found:
        print("***Room Price Is Invalid***")



# search rooms by availability
def search_by_availability():

    available_rooms_indexes, check_in_date, check_out_date = is_available()

    if available_rooms_indexes:
        for index in available_rooms_indexes:
            print(f"Hotel - {rooms[index].hotel_name} | Room Number - {rooms[index].room_number} | Room Type - {rooms[index].room_type} | Price - {rooms[index].price}")

    else:
        print("***No rooms available***")




def search_rooms():
    if rooms:

        print("Filter rooms by,\n")

        print("1. Type")
        print("2. Price")
        print("3. Availability")

        filter_rooms = input("\nEnter your choice: ")

        if filter_rooms == "1":
            search_by_type()

        elif filter_rooms == "2":
            search_by_price()

        elif filter_rooms == "3":
            search_by_availability()

        else:
            print("***Invalid choice***")
    else:
        print("\n***No rooms available***\n")
