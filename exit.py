from mongocontroller import mongoconnector

def handle_exit(vehicle_number,parking_id):
    try:
        parking_collection = mongoconnector("ParkingSite")
        p1 = parking_collection.find_one({"my_id": parking_id})

        vehicle_collection = mongoconnector("LiveVehicle")
        v1 = vehicle_collection.find_one({"vehicle_number":vehicle_number})

        slot_of_vehicle = v1['slot_number']
        type_of_vehicle = v1['vehicle_type']
        slots = p1['slots']
        empty_slots = p1['empty_slots']

        slots[slot_of_vehicle] = None
        empty_slots[type_of_vehicle].append(slot_of_vehicle)

        vehicle_collection .delete_one({ "vehicle_number" : vehicle_number})
        parking_collection.update_one({"my_id": parking_id}, {"$set": {"empty_slots": empty_slots, "slots": slots}})



    except:
        print("Something went wrong")
        return "Exit Unsuccessful"
    


if __name__ == "__main__":
    # testing
    handle_exit("hr245","ps1")

    