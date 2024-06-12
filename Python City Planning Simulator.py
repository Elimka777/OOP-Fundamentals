class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        """Save the building details to a file."""
        with open(filename, 'w') as file:
            file.write(f"{self.name},{self.floors}\n")

    @classmethod
    def load_from_file(cls, filename):
        """Load building details from a file."""
        with open(filename, 'r') as file:
            line = file.readline().strip()
            name, floors = line.split(',')
            return cls(name, int(floors))

# Script to demonstrate saving and loading buildings

# Creating multiple building instances
building1 = Building("Library", 3)
building2 = Building("City Hall", 5)
building3 = Building("Museum", 2)

# Save buildings to files
building1.save_to_file("building1.txt")
building2.save_to_file("building2.txt")
building3.save_to_file("building3.txt")

# Load buildings from files
loaded_building1 = Building.load_from_file("building1.txt")
loaded_building2 = Building.load_from_file("building2.txt")
loaded_building3 = Building.load_from_file("building3.txt")

# Print loaded buildings to verify
print(f"Loaded {loaded_building1.name} with {loaded_building1.floors} floors.")
print(f"Loaded {loaded_building2.name} with {loaded_building2.floors} floors.")
print(f"Loaded {loaded_building3.name} with {loaded_building3.floors} floors.")
