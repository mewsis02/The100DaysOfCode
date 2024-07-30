# My Python Calculator

import python_calculator_art
print(python_calculator_art.logo)


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    num1 = float(input("What's the first number: "))
    operations_text = "\nOperations: "
    for operation in operations:
        operations_text += operation + " "
    print(operations_text)
    operation_symbol = input("Pick an operation from the above: ")
    num2 = float(input("What's the second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    def run_new_operation(old_answer):
        keep_going = input(f"Type yes to continue calculating with {old_answer}, or no to use a new number: ").lower()
        if keep_going == "no":
            return "I am done."
        elif keep_going != "yes":
            print("That is not a valid response.\n")
            return "That is not a valid response."

        print(operations_text)
        operation_symbol = input("Pick another operation: ")
        new_number = float(input("Pick another number: "))
        calculation_function = operations[operation_symbol]
        new_answer = calculation_function(old_answer, new_number)

        if new_answer % 2 > 0:
            decimal_places = int(input("To how many decimal places: "))
            new_answer = round(new_answer, decimal_places)
            print(f"{old_answer} {operation_symbol} {new_number} rounded to {decimal_places} places = {new_answer}")
        else:
            print(f"{old_answer} {operation_symbol} {new_number} = {new_answer}")

        return new_answer

    temp_answer = answer
    while temp_answer != "I am done.":
        temp_answer = run_new_operation(answer)
        if temp_answer != "That is not a valid response.":
            answer = temp_answer
    print("\n")
    calculator()

calculator()