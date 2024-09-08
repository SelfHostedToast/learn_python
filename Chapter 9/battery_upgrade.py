# 9-9 Battery Upgrade

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
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
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount tothe odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a bettery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size <= 40:
            range = 150
        elif self.battery_size > 40:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size < 65:
            print('Upgrading Battery Capacity!')
            self.battery_size = 65
        else:
            self.battery_size = self.battery_size

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

print('Cars in my future garage:\n')
my_electric_car = ElectricCar('tesla', 'cyber truck', '2024')
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.fill_gas_tank()
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.describe_battery()

my_gas_car = Car('kia', 'soul', '2016')
print(my_gas_car.get_descriptive_name())