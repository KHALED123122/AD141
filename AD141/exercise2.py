#!/usr/bin/env python3

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name
initials = first_name[0].upper() + last_name[0].upper()

print("Full name:", full_name)
print("Initials:", initials)