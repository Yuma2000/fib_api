def fibonacci(n: int) -> int:
    """
    n番目のフィボナッチ数を計算して返す．

    Parameters:
    - n (int): フィボナッチ数列のn番目の値を取得するための整数。nは0以上である必要がある。

    Returns:
    - int: フィボナッチ数列のn番目の値。
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
