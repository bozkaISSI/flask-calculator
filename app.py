"""
Flask web application that provides a simple calculator via GET requests.
Supported operations: sum, subtract, multiply, divide.
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """
    Endpoint that performs basic arithmetic operations based on the 'operation' parameter.
    Supported operations: sum, subtract, multiply, divide.

    Arguments:
    - operation: The operation to perform ('sum', 'subtract', 'multiply', 'divide')
    - arg1: The first number (integer)
    - arg2: The second number (integer)

    Returns:
    - The result of the operation or an error message if the operation is invalid.
    """
    operation = request.args.get('operation', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if operation == 'sum':
        result = arg1 + arg2
    elif operation == 'subtract':
        result = arg1 - arg2
    elif operation == 'multiply':
        result = arg1 * arg2
    elif operation == 'divide' and arg2 != 0:
        result = arg1 / arg2
    else:
        result = 'Invalid operation or division by zero'

    return f'Result: {result}'


if __name__ == '__main__':
    app.run(debug=True)
