from data.save_data import rooms
from features.get_details import is_available

def view_available_rooms():

    if rooms:

        available_rooms_indexes, check_in_date, check_out_date = is_available()

        if available_rooms_indexes:
            print(f"\n | {len(available_rooms_indexes)} Rooms Available |")

        else:
            print("***No rooms available***")

    else:
        print("\n***No rooms available***\n")
