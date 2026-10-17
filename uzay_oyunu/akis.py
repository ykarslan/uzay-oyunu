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

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her adımda yakıtı tüketim kadar azaltıp kalan yakıtı üreten üreteç.

    Yakıt 0'a inince veya altına düşünce 0 üretip durur.
    """
    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan