from statistics import variance
from typing import Dict, List
from flask import jsonify, request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        
        media = self.__process_data(input_data)
        self.__verify_result(media)

        response = self.__format_response(media)
        return response 
    
    def __verify_result(self, media: float) -> None:
        if media <= 0:
            raise HttpBadRequestError("falha no processo: media invalida")
    
    def __validate_body(self, body: Dict) -> List[float]:
        if not body or "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        numbers = body["numbers"]

        if not isinstance(numbers, list) or len(numbers) == 0:
            raise HttpUnprocessableEntityError("numbers deve ser uma lista não vazia")
        
        return numbers
    
    def __process_data(self, input_data: List[float]) -> float:
        return sum(input_data) / len(input_data)
    

    def __format_response(self, media: float) -> Dict:
        return {
            "data": {
                "Calculator": "media",
                "value": round(media, 2),
                "Success": True
            }
        }