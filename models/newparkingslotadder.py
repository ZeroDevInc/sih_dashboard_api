import models.ParkingSiteModel as psm
from mongocontroller import mongoconnector

def add_data(name, total_slots, empty_slots, slots,my_id,price,threshold_value,increment,coordinates):
    parking_collection = mongoconnector("ParkingSite")
    ps = psm.ParkingSite(name, total_slots, empty_slots, slots,my_id,price,threshold_value,increment,coordinates)
    psData = ps.send_parking_site_data()
    parking_collection.insert_one(psData)

if __name__=='__main__':
    empty_slot=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    slots = ["0"]*100

    add_data("Chaitanya Parking",[500,400,300],empty_slot,slots,"ps1",[25,28,30],0.8,0.8,[0,5])