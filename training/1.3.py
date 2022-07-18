'''3. Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.'''
def string_from_both_ends(string):
  if len(string) < 2:
    return 'empty string'

  return string[0:2] + string[-2:]

print(string_from_both_ends('w3resource'))
print(string_from_both_ends('w'))
