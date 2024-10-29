##!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
This file is part of unit_converter 
(https://github.com/satya25/unit_converter). 
unit_converter is free software repository: 
You can redistribute it and/or modify it under 
the terms of the MIT License. 
unit_converter is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
MIT License for more details. 
You should have received a copy of the MIT License along with 
unit_converter. If not, see <https://opensource.org/licenses/MIT>.
"""
# ----------------------------------------------------------------------------
# File Name         :        ./unit_converter/unit_converter/temperature.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Oct 29, 2024
# Version           :       1.0
# Release           :       R1
# Dependencies      :       None (or list any dependencies)
# Usage             :       Import this module in your Python scripts.
# ----------------------------------------------------------------------------
# Credits and Acknowledgements
# - Special thanks to the Python community for their excellent work:
#   https://www.python.org/community/
# - The APIs used in this script are documented here:
#   https://docs.python.org/3/
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
# - Dataset(s) sourced from         :   -- NOT Applicable --
# - Inspiration drawn from          :   -- NOT Applicable --

# Thank you to the creators and maintainers of these resources!
# ----------------------------------------------------------------------------
# - Content Removal Requests
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at: spnigam25@yahoo.com
#   I will promptly remove the content upon request.
# ----------------------------------------------------------------------------

"""
This module provides functions for handling
conversions between different temperature units.
"""

## All imports whenever applicable come here.

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32
    
    