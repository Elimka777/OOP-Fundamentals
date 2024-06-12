# test_transportation.py

from public_transportation import Bus

# Creating bus instances
bus1 = Bus(101, 50)
bus2 = Bus(202, 40)
bus3 = Bus(303, 60)

# Accessing class attributes
print(f"City Name: {Bus.city_name}")
print(f"Base Fare: ${Bus.base_fare}")

# Accessing instance attributes and methods
print(bus1.display_info())
print(bus2.display_info())
print(bus3.display_info())
