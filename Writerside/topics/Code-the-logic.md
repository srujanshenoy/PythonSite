# Code the logic

## Thought Process
### Features needed
+ The calc must be able to take the previous output as the first number
+ This is so that the user can type like `2+3 +5 +6 /7` and so on.
+ Must be able to take any integer, -ve or +ve

### Code structure
+ Ask for
    + a (first number)
    + opperator
    + b (second number if prev. result 0 else the number)
+ calculate result by `+, -, *, /` ing a and b
+ store result to use for recursion

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
    
def calc(previous_result: float):
    
```

