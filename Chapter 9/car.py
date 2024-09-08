class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        # An attribute can be defined without being passed in as params
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Seet the odometer reading to the given value."""
        self.odometer_reading += mileage

my_dream_car = Car('honda', 'civic type R', 2024)
print(f"I have purchased my dream car, it's a {my_dream_car.get_descriptive_name()}.")
my_dream_car.read_odometer()

# Car gets delivered from manufacturer
# Updating an attribute value directly
print(f"My {my_dream_car.get_descriptive_name()} has been deilivered!")
my_dream_car.odometer_reading = 23
my_dream_car.read_odometer()


# Using our new update_odometer() method, we update the mileage reading attribute value
my_dream_car.update_odometer(7)
my_dream_car.read_odometer()
