import re

from apps.exception import ExceptDivisionByZero
from apps.operation_simple import somme, soustraction, multiplication, division, division_with_exception, \
    division_with_try_exception, division_with_try_and_return_code
from apps.operation_advanced import racine_carre


def main():
    """
    Read the fist number
    """
    first_number = int(input('Enter a number: '))

    """
    Read the fist number
    """
    second_number = int(input('Enter a second number: '))

    """
    Call somme()
    """
    somme_two_number = somme(first_number, second_number)
    print(f'somme: {first_number} + {second_number} = {somme_two_number}')

    """
    Call subraction()
    """
    substraction_two_number = soustraction(first_number, second_number)
    print(f'soustraction: {first_number} - {second_number} = {substraction_two_number}')

    """
    Call multiplication()
    """
    multiplication_two_number = multiplication(first_number, second_number)
    print(f'{first_number} * {second_number} = {multiplication_two_number}')

    """
    Call division()
    """
    division_two_number = division(first_number, second_number)
    print(f'division: {first_number} / {second_number} = {division_two_number}')

    """
    Call division_with_exception()
    """
    try:
        division_two_number_with_exception = division_with_exception(first_number, second_number)
        print(f'division_two_number_with_exception: {first_number} / {second_number} = '
              f'{division_two_number_with_exception}')
    except ExceptDivisionByZero:
        print('division_two_number_with_exception: Division by zero')

    """
    Call division_with_exception()
    """
    try:
        division_two_number_with_try_exception = division_with_try_exception(first_number, second_number)
        print(f'division_two_number_with_try_exception: '
              f'{first_number} / {second_number} = {division_two_number_with_try_exception}')
    except ExceptDivisionByZero:
        print('division_two_number_with_try_exception: Division by zero')

    """
    square root
    """
    racine_first_number = racine_carre(first_number)
    racine_second_number = racine_carre(second_number)
    print(f'sqrt({first_number})={racine_first_number}')
    print(f'sqrt({second_number})={racine_second_number}')

    message, division_result = division_with_try_and_return_code(first_number, second_number)
    if re.match('Ok', message):
        print(f'division_with_try_and_return_code: '
              f'{first_number} / {second_number} = {division_result} => message={message}')
    else:
        print(f'division_with_try_and_return_code: message={message}')


"""
in main call function main()
"""
if __name__ == '__main__':
    main()
