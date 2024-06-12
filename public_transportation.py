# public_transportation.py

class Bus:
    city_name = "Metropolis"
    base_fare = 2.50

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        return f"Bus Route: {self.route_number}, Capacity: {self.passenger_capacity}, City: {Bus.city_name}, Base Fare: ${Bus.base_fare}"

# Function to manage different bus routes (optional)
def manage_routes():
    # This can be extended to manage multiple routes, add buses, etc.
    pass
