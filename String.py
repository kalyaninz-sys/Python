user_string = input("Enter a string: ")


string_length = len(user_string)
print(f"The length of the string is: {string_length}")


print("\nPrinting each character individually: ")
for char in user_string:
    print(char)


print("\nDemonstrating string slicing: ")
if string_length >= 3:
    print(f"First 3 characters ([:3]): {user_string[:3]}")
    print(f"Last 3 characters ([-3:]): {user_string[-3:]}")
    print(f"String reversed ([::-1]): {user_string[::-1]}")
else:
    print(f"String reversed ([::-1]): {user_string[::-1]}")