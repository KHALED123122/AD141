#!/usr/bin/env python3

sentence = input("Enter a sentence: ")

first_char = sentence[0]
last_char = sentence[-1]

print(f"First character: '{first_char}', occurs {sentence.count(first_char)} times")
print(f"Last character: '{last_char}', occurs {sentence.count(last_char)} times")