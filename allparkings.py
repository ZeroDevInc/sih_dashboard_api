from mongocontroller import mongoconnector


def all_parkings():
    parking_collection = mongoconnector("ParkingSite")
    projection = {"my_id": 1, "name": 1, "total_slots": 1,"empty_slots":1, "price":1,  "_id":0}
    parking_sites = parking_collection.find({}, projection)
    return list(parking_sites)





if __name__ == '__main__':
    print(all_parkings())

