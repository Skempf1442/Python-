string1 = "hello"
capitalized_string = string1.capitalize()
print("Task 1 - Capitalize:", capitalized_string)

string2 = "hello"
centered_string = string2.center(10, '*')
print("Task 2 - Center:", centered_string)

string3 = "hello"
ends_with_lo = string3.endswith("lo")
print("Task 3 - Ends with 'lo':", ends_with_lo)

index = string3.find("lo")
print("Task 4 - Index of 'lo':", index)

string4 = "hello123"
is_alnum = string4.isalnum()
print("Task 5 - Is alphanumeric:", is_alnum)

is_alpha = string1.isalpha()
print("Task 6 - Is alphabetic:", is_alpha)

is_lower = string1.islower()
print("Task 7 - Is lowercase:", is_lower)

whitespace_string = "    "
is_space = whitespace_string.isspace()
print("Task 8 - Is whitespace:", is_space)

uppercase_string = "HELLO"
is_upper = uppercase_string.isupper()
print("Task 9 - Is uppercase:", is_upper)

joined_string = "-".join(["hello", "world"])
print("Task 10 - Joined string:", joined_string)

lowercase_string = uppercase_string.lower()
print("Task 11 - Lowercase:", lowercase_string)

leading_space_string = "  hello"
stripped_string = leading_space_string.lstrip()
print("Task 12 - Stripped leading spaces:", stripped_string)

trailing_space_string = "hello  "
trailing_stripped_string = trailing_space_string.rstrip()
print("Task 13 - Stripped trailing spaces:", trailing_stripped_string)

replaced_string = "hello world".replace("world", "Python")
print("Task 14 - Replaced substring:", replaced_string)

highest_index = string3.rfind("l")
print("Task 15 - Highest index of 'l':", highest_index)

split_string = "hello world".split()
print("Task 16 - Split string:", split_string)

starts_with_he = string3.startswith("he")
print("Task 17 - Starts with 'he':", starts_with_he)

strip_string = "  hello  ".strip()
print("Task 18 - Stripped both sides:", strip_string)

swapped_case_string = "Hello World".swapcase()
print("Task 19 - Swapped case:", swapped_case_string)

title_string = "hello world".title()
print("Task 20 - Title case:", title_string)

uppercase_conversion = string1.upper()
print("Task 21 - Uppercase:", uppercase_conversion)
