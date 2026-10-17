"""
akis.py - Üreteçler ve veri akış boru hattı modülü.
"""
from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    """
    Sonsuz Fibonacci sayı dizisi üreten üreteç.
    İlk değerler 0 ve 1 olarak başlar.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b