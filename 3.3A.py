# Prompt the user for two distinct integers 

num1 = int(input("Enter an integer: ")) 
num2 = int(input("Enter another integer: ")) 

# Logical comparisons using the 'and' operator 

print(f"Both numbers greater than 0: {num1 > 0 and num2 > 0}") 
print(f"Both numbers less than 50: {num1 < 50 and num2 < 50}") 
# Logical comparisons using the 'or' operator 

print(f"Either number is even: {num1 % 2 == 0 or num2 % 2 == 0}") 
print(f"Either number is greater than 100: {num1 > 100 or num2 > 100}") 

# Logical comparisons using the 'not' operator 

print(f"num1 is not equal to num2: {not (num1 == num2)}") 
print(f"num1 is not 0: {not (num1 == 0)}") 