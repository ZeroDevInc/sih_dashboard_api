class ParkingSite:
    def __init__(self, name, total_slots, empty_slots, slots,my_id,price,threshold_value,increment,coordinates,address):
        self.name = name
        self.total_slots = total_slots
        self.empty_slots = empty_slots
        self.slots = slots
        self.my_id = my_id
        self.price = price
        self.threshold_value = threshold_value
        self.increment = increment
        self.coordinates= coordinates
        self.address= address

        
    def send_parking_site_data(self):
        return {
            "name": self.name,
            "total_slots": self.total_slots,
            "empty_slots": self.empty_slots,
            "slots": self.slots,
            "my_id":self.my_id,
            "price":self.price,
            "threshold_value":self.threshold_value,
            "increment": self.increment,
            "coordinates":self.coordinates,
            "address":self.address
        }

