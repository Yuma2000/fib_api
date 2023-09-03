import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from fibonacci_calculator import fibonacci

load_dotenv()

app = Flask(__name__)
MAX_N_VALUE = 100000


@app.route('/', methods=['GET'])
def index():
    """
    このAPIの使用方法を示す情報を返す。

    Returns:
    - json: APIの使用方法を示す情報。
    - int: HTTPステータスコード
    """
    usage = {
        "message": "Welcome to the Fibonacci API!",
        "usage": {
            "endpoint": "/fib",
            "method": "GET",
            "parameters": {
                "n": "An integer value for which you want to get the Fibonacci number."
            },
            "headers": {
                "Content-Type": "application/json"
            }
        }
    }
    return jsonify(usage), 200


def create_error_response(status_code, message):
    """
    エラーメッセージを含むJSONレスポンスを作成し、返す。

    Parameters:
    - status_code (int): HTTPステータスコード
    - message (str): エラーメッセージ

    Returns:
    - json: エラーメッセージを含むJSON。
    - int: HTTPステータスコード
    """
    return jsonify({"status": status_code, "message": message}), status_code


@app.route('/fib', methods=['GET'])
def get_fibonacci():
    """
    フィボナッチ数列のn番目の値を計算して返す。

    Returns:
    - json: フィボナッチ数列のn番目の値。
    - int: HTTPステータスコード

    Raises:
    - ValueError: 不正なパラメータ値の場合。
    """
    try:
        # リクエストヘッダーがJSON形式かどうか確認する
        if request.headers.get("Content-Type") != "application/json":
            return create_error_response(400, "Invalid header. Expected Content-Type: application/json.")

        n_str = request.args.get('n')
        if not n_str:
            return create_error_response(400, "Parameter 'n' is missing.")
        if not n_str.isdigit():
            return create_error_response(400, "Parameter 'n' should be a positive integer.")

        n = int(n_str)
        if n == 0:
            raise ValueError("Parameter 'n' should be a positive integer.")
        if n > MAX_N_VALUE:
            raise ValueError(f"Value too large. Maximum allowed is {MAX_N_VALUE}.")

        result = fibonacci(n)
        return jsonify({"result": result}), 200

    except ValueError as e:
        return create_error_response(400, str(e))
    except Exception:
        return create_error_response(500, "Internal Server Error.")


if __name__ == "__main__":
    DEBUG_MODE = os.environ.get('DEBUG_MODE', 'False').lower() == 'true'
    app.run(debug=DEBUG_MODE)
