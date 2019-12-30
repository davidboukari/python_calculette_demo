import pytest
from apps.operation_simple import somme, soustraction, multiplication, division, division_with_exception
from apps.exception import ExceptDivisionByZero


class TestOperationSimple:
    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(1, 2, 3), (5, 4, 9)],)
    def test_somme_return_somme_of_two_numbers(number_1: int, number_2: int, excepted):
        assert somme(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(4, 3, 1), (5, 10, -5)],)
    def test_soustraction_return_soustraction_of_two_numbers(number_1: int, number_2: int, excepted):
        assert soustraction(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(4, 3, 12), (10, 5, 50)],)
    def test_multiplication_return_multiplication_of_two_numbers(number_1: int, number_2: int, excepted):
        assert multiplication(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(10, 2, 5), (64, 2, 32)],)
    def test_division_return_division_of_two_numbers(number_1: int, number_2: int, excepted):
        assert division(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2",  [(10, 0)],)
    def test_division_return_division_by_zero_it_return_error(number_1: int, number_2: int):
        assert division(number_1, number_2) == 'Error'

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(10, 5, 2)],)
    def test_division_with_exception_it_return_the_division(number_1: int, number_2: int, excepted):
        assert division_with_exception(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2",  [(10, 0)],)
    def test_division_with_exception_by_zero_return_an_execption(number_1: int, number_2: int):
        with pytest.raises(ExceptDivisionByZero):
            division_with_exception(number_1, number_2)

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2, excepted",  [(100, 20, 5)],)
    def test_division_with_try_exception_it_return_the_division(number_1: int, number_2: int, excepted):
        assert division_with_exception(number_1, number_2) == excepted

    @staticmethod
    @pytest.mark.parametrize("number_1, number_2",  [(10, 0)],)
    def test_division_with_try_exception_by_zero_return_an_execption(number_1: int, number_2: int):
        with pytest.raises(ExceptDivisionByZero):
            division_with_exception(number_1, number_2)
