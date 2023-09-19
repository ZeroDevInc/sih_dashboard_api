from mongocontroller import mongoconnector


def parking_detail(parking_id):
    parking_collection = mongoconnector("ParkingSite")
    slot = parking_collection.find_one({'my_id':parking_id})

    
    return {
        "name" : slot['name'],
        "price": slot["price"],
        "max_slots": slot["total_slots"],
        "available_slots": slot['empty_slots']
    }





if __name__ == '__main__':
    print(parking_detail("ps1"))
