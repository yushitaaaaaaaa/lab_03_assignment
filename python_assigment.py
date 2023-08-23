flight_d = {
    "AI161E90": ("BLR", "BOM", 5600),
    "BR161F91": ("BOM", "BBI", 6750),
    "AI161F99": ("BBI", "BLR", 8210),
    "VS171E20": ("JLR", "BBI", 5500),
    "AS171G30": ("HYD", "JLR", 4400),
    "AI131F49": ("HYD", "BOM", 3499)
}

c_c = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"

}

def get_flight_details(flight_id=None, s_c=None, destination=None):
    if flight_id:
        if flight_id in flight_d:
            source, dest, price = flight_d[flight_id]
            print(f"Flight ID: {flight_id}")
            print(f"Source: {c_c[source]}")
            print(f"Destination: {c_c[dest]}")
            print(f"Price: {price}")
        else:
            print("Flight not found.")
    elif s_c:
        match = [(fid, source, dest, price) for fid, (source, dest, price) in flight_d.items() if source == s_c]
        if match:
            print("Flights from", c_c[s_c])
            for fid, source, dest, price in match:
                print(f"Flight ID: {fid}")
                print(f"Destination: {c_c[dest]}")
                print(f"Price: {price}")
        else:
            print("No flights found from", c_c[s_c])
    elif destination:
        match = [(fid, source, dest, price) for fid, (source, dest, price) in flight_d.items() if dest == destination]
        if match:
            print("Flights to", c_c[destination])
            for fid, source, dest, price in match:
                print(f"Flight ID: {fid}")
                print(f"Source: {c_c[source]}")
                print(f"Price: {price}")
        else:
            print("No flights found to", c_c[destination])
    else:
        print("Please provide valid input.")

user_input_type = int(input("Enter 1 for Flight ID, 2 for source city, or 3 for destination city: "))
if user_input_type == 1:
    flight_id = input("Enter Flight ID: ")
    get_flight_details(flight_id=flight_id)
elif user_input_type == 2:
    s_c = input("Enter source city: ")
    get_flight_details(s_c=s_c)
elif user_input_type == 3:
    destination = input("Enter destination city: ")
    get_flight_details(destination=destination)
else:
    print("Invalid input type.")