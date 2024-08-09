# Prompt user to enter a class method
classmethod = int(input('Enter cm (1 , 2 , 3 ): '))

# Prompt user to enter an operation
vas = int(input('Enter op (1 for addition, 2 for subtraction, 3 for multiplication): '))

# Check the value of classmethod and print the corresponding message
if vas == 1:
    print("op set to addition")
elif vas == 2:
    print("op set to subtraction")
elif vas == 3:
    print("op set to multiplication")

# Prompt user to enter another class method
a = int(input('2 Enter cm: '))

# Print the set message and the operation value
print("set 2nd cm")
opration = vas

# Perform the operation based on user input
if opration == 1:
    result = classmethod + a
    print(f"Result of addition: {result}")
elif opration == 2:
    result = classmethod - a
    print(f"Result of subtraction: {result}")
elif opration == 3:
    result = classmethod * a
    print(f"Result of multiplication: {result}")
else:
    print("Invalid operation")


