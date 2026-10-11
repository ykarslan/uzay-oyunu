# Görev 4 (b) - Kapsam ve UnboundLocalError İncelemesi

## Örnek 1: Yerel Kapsam (Local Scope)
x = 10

def goster():
    x = 20
    print("Fonksiyon içi:", x)

goster()
print("Fonksiyon dışı:", x)

## Örnek 2: Global DeğişkeneErişim


x = 10

def goster():
    x = 20
    print("Fonksiyon içi:", x)

goster()
print("Fonksiyon dışı:", x)

## Örnek 3: UnboundLocalError

x = 10

def guncelle():
    x = x + 1
    print(x)

guncelle()