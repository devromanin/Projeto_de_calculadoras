from src.calculators.calculator_2 import Calculator2
from src.drivers import numpy_handler
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler) # type: ignore
    return calc

