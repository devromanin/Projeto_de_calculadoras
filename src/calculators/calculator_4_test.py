from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    pass

def test_calculate_with_invalid_body():
    mock_request = MockRequest({})
    calculator_4 = Calculator4(MockDriverHandler()) # type: ignore

    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado"


def test_calculate_with_invalid_average():
    mock_request = MockRequest({ "numbers": [-10, -20]})
    calculator_4 = Calculator4(MockDriverHandler()) # type: ignore

    with raises(HttpBadRequestError) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "falha no processo: media invalida"

def test_calculate_success():
    mock_request = MockRequest({ "numbers": [10, 20, 30] })
    calculator_4 = Calculator4(MockDriverHandler()) # type: ignore

    response = calculator_4.calculate(mock_request)

    assert response == {
        "data": {
            "Calculator": "media",
            "value": 20.0,
            "Success": True
        }
    }