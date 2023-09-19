class Vehicle:
    def __init__(self, vehicle_number: str, vehicle_type: int, start_time: int, end_time: int, slot_number: int,parking_id:str):
        if not isinstance(vehicle_number, str):
            raise ValueError("vehicle_number must be a string")
        if not isinstance(vehicle_type, int):
            raise ValueError("vehicle_type must be an integer")
        if not isinstance(start_time, int):
            raise ValueError("start_time must be an integer")
        if not isinstance(end_time, int):
            raise ValueError("end_time must be an integer")
        if not isinstance(slot_number, int):
            raise ValueError("slot_number must be an integer")
        if not isinstance(parking_id, int):
            raise ValueError("parking_id must be an integer")

        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.start_time = start_time
        self.end_time = end_time
        self.slot_number = slot_number
        self.parking_id = parking_id

    def send_vehicle_data(self):
        vehicle_data = {
            "vehicle_number": self.vehicle_number,
            "vehicle_type": self.vehicle_type,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "slot_number": self.slot_number,
            "parking_id":self.parking_id
        }
        
        return vehicle_data 