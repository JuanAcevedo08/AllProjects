from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> int:
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> int:
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    if b == 0:
        raise ZeroDivisionError("DO NOT DIVIDE BY 0")
    else:
        return a / b

if __name__ == '__main__':
    add()
    subtract()
    multiply()
    divide()
