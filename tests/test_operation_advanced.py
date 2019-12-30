import pytest
from apps.operation_advanced import racine_carre

ROOT_APP_PATH = 'apps'
ADVANCED_SQRT_PATH = f"{ROOT_APP_PATH}.operation_advanced.sqrt"


class TestOperationAdvanced:
    @staticmethod
    @pytest.mark.parametrize("number, excepted", [(9, 3.0)],)
    def test_racine_carre_it_return_sqrt(number: float, excepted):
        assert racine_carre(number) == excepted

    @staticmethod
    @pytest.mark.parametrize("number", [9], )
    def test_racine_carre_it_call_sqrt_at_once(mocker, number: float):
        mock_sqrt = mocker.patch(ADVANCED_SQRT_PATH)
        racine_carre(number)
        mock_sqrt.assert_called_once_with(number)
