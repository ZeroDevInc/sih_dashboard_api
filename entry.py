from mongocontroller import mongoconnector

def entry(vehicle_number):
    vehicle_collection = mongoconnector("LiveVehicle") 
    vehicle = vehicle_collection.find_one({"vehicle_number": vehicle_number})

    if vehicle is None:
        return "Bhai phle slot book to krle"
    else:
        return "Welcome bhai"


if __name__ == '__main__':
    print(entry("hr24565646"))
