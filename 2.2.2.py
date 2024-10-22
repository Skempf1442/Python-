print("Common Escape Sequences:")
print("Newline: 'Hello\nWorld'")
print("Horizontal Tab: 'Hello\tWorld'")
print("Backslash: '\\'")
print("Single Quote: 'It\'s a string'")
print("Double Quote: \"He said, 'Hello'\"")
print("Carriage Return: 'Hello\rWorld'")
print("Backspace: 'Hello\bWorld'")

multi_line_string = """This is an example
of a multiline
string in Python."""
print("\nMultiline String:")
print(multi_line_string)

combined_string = "Hello" + " " + "World"
print("\nConcatenation Example:")
print(combined_string)  # Output: Hello World

repeated_string = "Python! " * 3
print("\nReplication Example:")
print(repeated_string)  # Output: Python! Python! Python!

word = "Hello"
print("\nIterating through the string:")
for char in word:
    print(char)  # Prints each character

text = "hello"
print("\nMax and Min in String:")
print("Max:", max(text))  # Output: 'o'
print("Min:", min(text))  # Output: 'e'

word = "Python"
print("\nIndex of 't' in 'Python':", word.index("t"))  # Output: 2

string = "Python"
list_of_chars = list(string)
print("\nString to List:")
print(list_of_chars)  # Output: ['P', 'y', 't', 'h', 'o', 'n']

sentence = "This is a test sentence."
print("\nCount of 't' in the sentence:")
print(sentence.count("t"))  # Output: 5

example_string = "Hello World"
sliced_string = example_string[6:]  # Gets 'World'
print("\nSlicing Example:")
print(sliced_string)  # Output: World

check_string = "Hello Python World"
print("\nCheck if 'Python' is in the string:")
print("Python" in check_string)  # Output: True

print("\nCheck if 'Java' is not in the string:")
print("Java" not in check_string)  # Output: True
