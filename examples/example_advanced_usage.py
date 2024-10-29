# example_advanced_usage.py

from unit_converter.weight import kilograms_to_pounds, grams_to_ounces
from unit_converter.speed import kilometers_per_hour_to_miles_per_hour
from unit_converter.pressure import pascals_to_atmospheres

def main():
    # Weight conversions
    kg = 70
    lbs = kilograms_to_pounds(kg)
    print(f"{kg} kg is equal to {lbs:.2f} lbs.")

    g = 1000
    oz = grams_to_ounces(g)
    print(f"{g} g is equal to {oz:.2f} oz.")

    # Speed conversion
    kmh = 100
    mph = kilometers_per_hour_to_miles_per_hour(kmh)
    print(f"{kmh} km/h is equal to {mph:.2f} mph.")

    # Pressure conversion
    pa = 101325
    atm = pascals_to_atmospheres(pa)
    print(f"{pa} Pa is equal to {atm:.2f} atm.")

if __name__ == "__main__":
    main()
    
    