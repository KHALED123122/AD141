#!/usr/bin/env python3

text = input("Enter a string: ")

print("Ends with period:", text.endswith('.'))
print("All alphabetic:", text.isalpha())
print("'x' in string:", 'x' in text)
print("Replace e with E:", text.replace('e', 'E'))