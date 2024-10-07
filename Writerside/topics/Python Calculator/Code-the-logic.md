# Code the logic

## Thought Process
### Features needed
+ The calc must be able to take the previous output as the first number
+ This is so that the user can type like `2+3 +5 +6 /7` and so on.
+ Must be able to take any integer, -ve or +ve

## CODE
```python
def int_input(prompt):
    try:
        return int(input(prompt))
    except:
        print("Enter an actual number...")
        return int_input(prompt)

def opperator_input():
    user_input = input("enter an opperator: ")
    return user_input if user_input in ["+", "-", "x", "/"] else opperator_input()

def continue_calc():
    usr_in = input("Continue? (enter for yes, anything else for a no.")
    return False if usr_in != '' else True
    
def calc(previous_result: float, starting: bool):
    # Get the inputs
    a = int_input("Enter the first number: ") if starting else previous_result
    b = int_input("Enter the second number: ")
    opperator = opperator_input()

    # Initialize and get result
    result = 0

    if opperator == '+':
        result = a + b
    elif opperator == '-':
        result = a - b
    elif opperator == 'x':
        result = a * b
    elif opperator == '/':
        result = (a/b) if b != 0 else 0 # Error handling of zero division errors

    # Print the result as an equation
    
    print(f"{a} {opperator} {f"({b})" if (b < 0) else b} = {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""} ")
    # This line started as
    # print(f"{a} {opperator} {b} = {result}")
    #
    # Then, for appearance, if the user inputs a negative number for b, it should be represented as (-b)
    # So for brackets and the check together, the {b} became
    #                                             {f"({b})" if (b < 0) else b}
    #                                                  - sign in b value itself
    #
    # Then, for the zero division errors, it should be represented as [RESET: Zero division error]
    # So for the check and the brackets together, the {result} became
    #                                             {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""}

    

    if continue_calculating(): return calc(result, False)
    else: return result
    
#Start the program
if __name__ == '__main__':
    calc(0, True)
``` 
