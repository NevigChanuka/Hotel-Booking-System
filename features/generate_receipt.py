# print receipt
def generate_receipt(customer_name,customer_age, contact_number, hotel_name, room_type, room_number, check_in_date, check_out_date):

    gene_receipt = input("\nDo you want to get a receipt ? (yes/no): ").lower()

    if gene_receipt == "yes":
        print(f"\n Customer Name  = {customer_name}"
              f"\n Customer Age   = {customer_age}"
              f"\n Contact Number = {contact_number}"
              f"\n Hotel Name     = {hotel_name}"
              f"\n Room Type      = {room_type}"
              f"\n Room Id        = {room_number}"
              f"\n Check In Date  = {check_in_date}"
              f"\n Check out Date = {check_out_date}")

    elif gene_receipt == "no":
        pass
    else:
        print("\n****Invalid input****")
