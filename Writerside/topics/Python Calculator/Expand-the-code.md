# Expand the code

## Expansion 1: Accepting floats
+ Instead of only accepting number like 1, 2, 3, 4, ...
+ Let us make our calculator accept numbers like 2.56, 3.123567, etc.

### Process
+ We have used the function `int_input()` in our code to take the numbers.
+ This function only accepts integers
+ We want it to also accept floats.
+ to do this, we just need to change
  + The name of the function,
  + the `int()` to `float()` in the try-except block and return block
  + and the usage of the function name everywhere.

#### 1. Change the function name
```python
def float_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return int_input(prompt)
```

#### 2. Change int() to float()
```python
def float_input(prompt: str) -> int:
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return float_input(prompt)
```

#### 3. Change the function name in the code (full code below) {collapsible="true"}
```python
def float_input(prompt: str) -> int:
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return float_input(prompt)


def opperator_input():
    user_input = input("Enter an opperator(+, -, x, *, /): ")
    if user_input in ['+', '-', 'x', '/']:
        return user_input
    else:
        return opperator_input()


def continue_calculating():
    user_input = input("Continue? (enter for yes, anything else for no): ")
    return user_input == ""  # This line checks if the user's input is empty. If it is, returns True, else false.


def calc(previous_result: float, starting: bool):
    a = float_input("Enter the first number: ") if starting else previous_result
    opperator = opperator_input()
    b = float_input("Enter the second number: ")

    result = 0

    if opperator == '+':
        result = a + b
    elif opperator == '-':
        result = a - b
    elif opperator == 'x':
        result = a * b
    elif opperator == '/':
        result = (a/b) if b != 0 else 0



    print(f"{a} {opperator} {f"({b})" if (b < 0) else b} = {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""} ")
    # This line started as
    # print(f"{a} {opperator} {b} = {result}")
    #
    # Then, for appearance, if the user inputs a negative number for b, it should be represented as (-b)
    # So for brackets and the check together, the {b} became
    #                                             {f"({b})" if (b < 0) else b}
    #
    # Then, for the zero division error, it should be represented as [RESET: Zero division error]
    # So for the check and the brackets together, the {result} became
    #                                             {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""}



    if continue_calculating(): return calc(result, False)
    else: return result

if __name__ == '__main__':
    calc(0, True)
```

## Expansion 2: Accepting more operations
+ Now that we have expanded the numbers, what else is there?
+ Right! The operations!
+ Currently, it takes +, -, x and /
+ We want it to take +, -, x, *, **, ^, nrt(nth root), /
+ Square root has to be inputted as nrt 2
+ To do this, we need to change the `opperator_input()` function. Specifically, we need to change the list in it

+ Current code, Changed list code
<code-block lang="python" collapsible="true">
def opperator_input():
    user_input = input("Enter an opperator(+, -, x, *, /): ")
    if user_input in ['+', '-', 'x', '/']:
        return user_input
    else:
        return opperator_input()
</code-block>
<code-block lang="python" collapsible="true">
def opperator_input():
    user_input = input("Enter an opperator(+, -, x, *, x, ^, **, nrt, /): ")
    if user_input in ['+', '-', 'x', '/', '*', '**', '^', 'nrt']:
        return user_input
    else:
        return opperator_input()
</code-block>

+ Now, to add in the extra opperators *, **, ^, nrt
+ We have handled the operation code in this:
<code-block lang="python" collapsible="true">
    if opperator == '+':
        result = a + b
    elif opperator == '-':
        result = a - b
    elif opperator == 'x':
        result = a * b
    elif opperator == '/':
        result = (a/b) if b != 0 else 0
</code-block>

+ To add these opperators, we need these lines in it:
  + First, change the line `elif opperation == 'x' ` to `elif opperation == ('x' or '*'): `
  + Then add the following four lines for **, ^, and nth root:
<code-block lang="python">
elif opperation == ('**' or '^'):
    result = a ** b
elif opperation == 'nrt':
    result = a ** (1/b)
</code-block>

+ So now our code becomes
```python
def opperator_input():
    user_input = input("Enter an opperator(+, -, x, *, x, ^, **, nrt, /): ")
    if user_input in ['+', '-', 'x', '/', '*', '**', '^', 'nrt']:
        return user_input
    else:
        return opperator_input()

def calc(...):

    if opperator == '+':
        result = a + b
    elif opperator == '-':
        result = a - b
    elif opperator == ('x' or '*'):
        result = a * b
    elif opperator == '/':
        result = (a/b) if b != 0 else 0
    elif opperator == ('**' or '^'):
        result = a ** b
    elif opperator == 'nrt':
        result = a ** (1/b)
    
    ...
```
{collapsible="true" default-state="collapsed"}

## FINAL CODE
```python
def float_input(prompt: str) -> int:
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return float_input(prompt)


def opperator_input():
    user_input = input("Enter an opperator(+, -, x, *, x, ^, **, nrt, /): ")
    if user_input in ['+', '-', 'x', '/', '*', '**', '^', 'nrt']:
        return user_input
    else:
        return opperator_input()


def continue_calculating():
    user_input = input("Continue? (enter for yes, anything else for no): ")
    return user_input == ""  # This line checks if the user's input is empty. If it is, returns True, else false.


def calc(previous_result: float, starting: bool):
    a = float_input("Enter the first number: ") if starting else previous_result
    opperator = opperator_input()
    b = float_input("Enter the second number: ")

    result = 0

    if opperator == '+':
        result = a + b
    elif opperator == '-':
        result = a - b
    elif opperator == ('x' or '*'):
        result = a * b
    elif opperator == '/':
        result = (a/b) if b != 0 else 0
    elif opperator == ('**' or '^'):
        result = a ** b
    elif opperator == 'nrt':
        result = a ** (1/b)

    print(f"{a} {opperator} {f"({b})" if (b < 0) else b} = {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""} ")
    # This line started as
    # print(f"{a} {opperator} {b} = {result}")
    #
    # Then, for appearance, if the user inputs a negative number for b, it should be represented as (-b)
    # So for brackets and the check together, the {b} became
    #                                             {f"({b})" if (b < 0) else b}
    #
    # Then, for the zero division error, it should be represented as [RESET: Zero division error]
    # So for the check and the brackets together, the {result} became
    #                                             {result} {"[RESET: Zero division error]" if (b == 0 and opperator == '/') else ""}



    if continue_calculating(): return calc(result, False)
    else: return result

if __name__ == '__main__':
calc(0, True)

```
{collapsible="true" default-state="expanded"}

code on [GitHub](https://github.com/srujanshenoy/PythonSite/blob/master/Script%20files/Python%20Calculator/Python%20Calculator%20Opperation%20expantion.py)
