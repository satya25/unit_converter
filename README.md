# Unit Converter

A simple and efficient unit converter that allows for conversions between various units of length, area, temperature, volume, speed, energy, pressure, time, weight, and frequency.

## Features

- **Length**: Convert between meters, kilometers, miles, feet, and inches.
- **Area**: Convert between square meters, acres, hectares, and square kilometers.
- **Temperature**: Convert between Celsius, Fahrenheit, and Kelvin.
- **Volume**: Convert between liters, milliliters, gallons, and fluid ounces.
- **Speed**: Convert between meters per second (m/s), kilometers per hour (km/h), and miles per hour (mph).
- **Energy**: Convert between joules and calories.
- **Pressure**: Convert between Pascals (Pa), atmospheres (atm), bars, and millimeters of mercury (mmHg).
- **Time**: Convert between seconds, minutes, and hours.
- **Weight**: Convert between kilograms (kg), grams (g), pounds (lbs), and ounces (oz).
- **Frequency**: Convert between Hertz (Hz), kilohertz (kHz), megahertz (MHz), and gigahertz (GHz).

## Installation

You can install the package using Poetry:

```bash
poetry install
```

## Usage

Here is an example of how to use the unit converter:

from unit_converter.length import meters_to_kilometers

result = meters_to_kilometers(1000)
print(result)  # Output: 1.0

## Running Tests

To run the tests for this project:

python -m unittest discover -s tests


## Contributing

Contributions are welcome! Please see the CONTRIBUTING.md file for more information.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Inspired by various open-source projects.
Special thanks to contributors who help improve this project.


### Key Points:

- The **Usage** section provides a clear example of how to use the converter.
- The **Running Tests** section explains how to execute tests for the project. 