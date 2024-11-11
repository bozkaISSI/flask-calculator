"""
Flask web application that provides a simple calculator via GET requests.
Supported operations: sum, subtract, multiply, divide.
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """
    Endpoint that performs basic arithmetic operations based on the 'op' parameter.
    Supported operations: sum, subtract, multiply, divide.

    Arguments:
    - op: The operation to perform ('sum', 'subtract', 'multiply', 'divide')
    - arg1: The first number (integer)
    - arg2: The second number (integer)

    Returns:
    - The result of the operation or an error message if the operation is invalid.
    """
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op == 'sum':
        result = arg1 + arg2
    elif op == 'subtract':
        result = arg1 - arg2
    elif op == 'multiply':
        result = arg1 * arg2
    elif op == 'divide' and arg2 != 0:
        result = arg1 / arg2
    else:
        result = 'Invalid operation or division by zero'

    return f'Result: {result}'


if __name__ == '__main__':
    app.run(debug=True)
