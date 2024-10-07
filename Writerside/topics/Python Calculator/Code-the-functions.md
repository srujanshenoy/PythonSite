# Code the functions

Our current code:
```python
def intinput(prompt): pass
def opp_in(): pass
def continue_calc(): pass
```

## Int input {collapsible="true" default-state="expanded"}
+ to do this, we need a `try-except` block.

```python 
def int_input(prompt):
    try:
        return int(input(prompt))
    except:
        print("Enter an actual number...")
        return int_input(prompt)
```

+ This code uses the `try - except` block.
+ It tries to give the integer form (`int`), but if it encounters an error, it calls itself again, repeating the cycle

## Opperator input {collapsible="true" default-state="expanded"}
+ This uses recursion, just like the last function (`int_input()`)
+ So, we make the function like this
  + ask for user input
  + check if it is +, -, x, or /
  + If it is, return it
  + If not, call the function again.
  + So,
```python 
def opperator_input():
    user_input = input("enter an opperator: ")
    if user_input in ["+", "-", "x", "/"]:
        return user_input
    else: return opperator_input()
```

## Continue_calc {collapsible="true" default-state="expanded"}
+ This function should take no inputs
+ It should ask the user to answer one thing for yes or anything else for no.
+ And it should return `True` or `False` for its output
+ So...

```python 
def continue_calc():
    usr_in = input("Continue? (enter for yes, anything else for a no.)
    return False if usr_in != '' else return True
```

+ Now our code looks like 
```python
def int_input(prompt):
    try:
        return int(input(prompt))
    except:
        print("Enter an actual number...")
        return int_input(prompt)

def opperator_input():
    user_input = input("enter an opperator: ")
    return user_input if user_input in ["+", "-", "x", "/"] else return opperator_input()

def continue_calc():
    usr_in = input("Continue? (enter for yes, anything else for a no.")
    return False if usr_in != '' else return True
```

