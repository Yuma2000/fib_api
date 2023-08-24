## ドキュメント: フィボナッチAPIサービス

### 1. 概要

このサービスは、フィボナッチ数列の任意の項目を計算し、その結果をJSON形式で返すAPIを提供します。

### 2. ディレクトリとファイルの構成

```
/fibonacci_api
|-- /tests
|   |-- test_api.py
|-- app.py
|-- README.md
```

- `app.py`: アプリケーションのメインファイル。Flaskアプリケーションとフィボナッチ計算関数が含まれています。
- `/tests`: ユニットテストを格納するディレクトリ。
  - `test_api.py`: フィボナッチ関数とAPIエンドポイントのユニットテストを含む。
- `README.md`: アプリケーションの使用方法や詳細を説明するドキュメント。

### 3. 主な機能

#### 3.1. フィボナッチ関数

- ファイル: `app.py`
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

### 5. セットアップと実行方法

1. 必要なライブラリをインストール:

```bash
pip install Flask
```

2. アプリケーションの実行:

```bash
python3 app.py
```

このコマンドを実行すると、デフォルトで`http://127.0.0.1:5000/`でサーバが起動します。

3. ユニットテストの実行:

```bash
python3 -m unittest tests/test_api.py
```
