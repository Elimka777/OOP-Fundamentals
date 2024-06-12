# Task 1: Vehicle Registration System

# Define the Vehicle class
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        # Initialize the attributes: registration number, type, and owner
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner

# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

# Demonstrating changing the owner
print(f"Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
vehicle1.update_owner("Alice Johnson")
print(f"Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")

print(f"Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
vehicle2.update_owner("Bob Brown")
print(f"Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

# Task 2: Event Management System Enhancement

# Define the Event class
class Event:
    def __init__(self, name, date):
        # Initialize the attributes: name, date, and participant count
        self.name = name
        self.date = date
        self.participant_count = 0

    # Method to add a participant
    def add_participant(self):
        self.participant_count += 1

    # Method to get the current number of participants
    def get_participant_count(self):
        return self.participant_count

# Creating an instance of Event
event = Event("Tech Conference", "2024-09-12")

# Adding participants
event.add_participant()
event.add_participant()

# Retrieving the participant count
print(f"Event: {event.name}, Date: {event.date}, Participants: {event.get_participant_count()}")
