
class ExceptDivisionByZero(Exception):
    pass


def somme(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number to add
    :type nombre_1: int
    :param nombre_2: number to add
    :type nombre_2: int
    :return: return the sum ot the nombre_1 + nombre_2
    :rtype: int
    """
    return nombre_1 + nombre_2


def soustraction(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number
    :type nombre_1: int
    :param nombre_2: number to substract
    :type nombre_2: int
    :return: return the substraction ot the nombre_1 - nombre_2
    :rtype: int
    """
    return nombre_1 - nombre_2


def multiplication(nombre_1: int, nombre_2: int) -> int:
    """
    :param nombre_1: number
    :type nombre_1: int
    :param nombre_2: number
    :type nombre_2: int
    :return: return the substraction ot the nombre_1 * nombre_2
    :rtype: int
    """
    return nombre_1 * nombre_2


def division(nombre_1: int, nombre_2: int):

    if nombre_2 == 0:
        return 'Error'
    else:
        return nombre_1 / nombre_2


def division_with_exception(nombre_1: int, nombre_2: int):
    if nombre_2 == 0:
        message = 'division by zero'
        raise ExceptDivisionByZero(message)
    return nombre_1 / nombre_2


def division_with_try_exception(nombre_1: int, nombre_2: int):
    try:
        return nombre_1 / nombre_2
    except Exception:
        message = 'division by zero'
        raise ExceptDivisionByZero(message)


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
    print(f'{first_number} + {second_number} = {somme_two_number}')

    """
    Call subraction()
    """
    substraction_two_number = soustraction(first_number, second_number)
    print(f'{first_number} - {second_number} = {substraction_two_number}')

    """
    Call multiplication()
    """
    multiplication_two_number = multiplication(first_number, second_number)
    print(f'{first_number} * {second_number} = {multiplication_two_number}')

    """
    Call division()
    """
    division_two_number = division(first_number, second_number)
    print(f'{first_number} / {second_number} = {division_two_number}')

    """
    Call division_with_exception()
    """
    try:
        division_two_number_with_exception = division_with_exception(first_number, second_number)
        print(f'{first_number} / {second_number} = {division_two_number_with_exception}')
    except ExceptDivisionByZero:
        print('Division by zero')


"""
in main call function main()
"""
if __name__ == '__main__':
    main()
