# !/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 20, 2021
# This program converts celsius to  fahrenheit.
def calculate_farenheigt():
    user_degrees = input("Enter degrees in celsius: ")
    try:
        user_degrees_float = float(user_degrees)
        degrees_farenheight = (9.0/5.0)*user_degrees_float+32
        print("{}°C is equal to {}°F ".format(user_degrees_float, degrees_farenheight))
    except Exception:
        print("Invalid input")


calculate_farenheigt()
