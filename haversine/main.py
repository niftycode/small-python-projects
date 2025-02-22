"""
Small Python Projects for Beginners
Haversine - Calculate the great circle distance in kilometers between two points
on the Earth

Version: 1.0
Python 3.12
Author: AnaJuliaCodes
Date created: June 23th, 2024
Date modified: -
"""

import math


def haversine(lat1, lon1, lat2, lon2):
    # Calculates the harversine formula
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371.0 * c
    return distance


def checkFloat(num):
    # Checks if a string can be converted to a decimal number (float)
    try:
        num = float(num)
    except ValueError as ex:
        print(
            "Error: String contains characters that can't be converted to a decimal number"
        )
        print(ex)
        exit(1)
    return num


if __name__ == "__main__":
    lat1 = input("Enter latitude of first point: ")
    lat1 = checkFloat(lat1)
    lon1 = input("Enter longitude of first point: ")
    lon1 = checkFloat(lon1)
    lat2 = input("Enter latitude of second point: ")
    lat2 = checkFloat(lat2)
    lon2 = input("Enter longitude of second point: ")
    lon2 = checkFloat(lon2)
    distance = haversine(lat1, lon1, lat2, lon2)
    print("Distance: " + str(int(distance)) + " kilometers")
