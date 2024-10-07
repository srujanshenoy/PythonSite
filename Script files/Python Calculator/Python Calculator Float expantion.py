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