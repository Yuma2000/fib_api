from flask import Flask, request, jsonify

app = Flask(__name__)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        if n < 0:
            raise ValueError
        result = fibonacci(n)
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"status": 400, "message": "Bad request."}), 400


if __name__ == "__main__":
    app.run(debug=True)
