# example_basic_usage.py

from unit_converter.length import meters_to_kilometers
from unit_converter.temperature import celsius_to_fahrenheit
from unit_converter.volume import liters_to_gallons

def main():
    # Length conversion
    meters = 1000
    kilometers = meters_to_kilometers(meters)
    print(f"{meters} meters is equal to {kilometers} kilometers.")

    # Temperature conversion
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F.")

    # Volume conversion
    liters = 5
    gallons = liters_to_gallons(liters)
    print(f"{liters} liters is equal to {gallons} gallons.")

if __name__ == "__main__":
    main()