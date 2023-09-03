## フィボナッチ数API

### 1. 概要

このREST APIは、n番目のフィボナッチ数を計算し、その結果をJSON形式で返します。

### 2. ディレクトリとファイルの構成

```
/fib_api
|-- /tests
|   |-- test_api.py
|-- app.py
|-- fibonacci_calculator.py
|-- README.md
|-- requirements.txt
```

- `app.py`: アプリケーションのメインファイル。Flaskアプリケーションが含まれています。
- `fibonacci_calculator.py`: フィボナッチ数の計算関数が含まれています。
- `/tests`: ユニットテストを格納するディレクトリ。
  - `test_api.py`: フィボナッチ関数とAPIエンドポイントのユニットテストを含む。
- `README.md`: アプリケーションの使用方法や詳細を説明するドキュメント。
- `requirements.txt`: 必要なPythonパッケージのリスト。

### 3. 主な機能

#### 3.1. フィボナッチ関数

- ファイル: `fibonacci_calculator.py`
- 機能: 与えられた整数`n`に対して、フィボナッチ数列の`n`番目の項目を計算します。

#### 3.2. APIエンドポイント

- URL: `/fib`
- メソッド: `GET`
- クエリパラメータ: `n`（フィボナッチ数列のインデックス）
- レスポンス: 
  - 正常時: `{"result": <フィボナッチ数>}`
  - エラー時: `{"status": 400, "message": "Bad request."}`

### 4. 使用技術

- **Python**: プログラムの主要な言語。
- **Flask**: 軽量なWebフレームワーク。APIエンドポイントの実装に使用。
- **Gunicorn**: アプリのデプロイに使用。

### 5. セットアップと実行方法

1. 必要なライブラリをインストール:

```bash
pip install -r requirements.txt
```

2. アプリケーションの実行:

開発モード (Flaskのデフォルトサーバを使用):

```bash
python3 app.py
```
本番モード (gunicornを使用):

```bash
gunicorn app:app
```
このコマンドを実行すると、デフォルトで http://127.0.0.1:8000/ でサーバが起動します。異なるポートや設定で実行する場合は、gunicorn のドキュメントを参照してください。

3. ユニットテストの実行:

```bash
python3 -m unittest tests/test_api.py
```

### 6. 環境変数

このアプリケーションでは、`.env` ファイルを使用して環境変数を設定します。次の環境変数が必要です：

- DEBUG_MODE: デバッグモードを有効にするには True、無効にするには False を設定します。
