#görev 1
print ("Ad: Yusuf Kağan Arslan")
print ("Bölüm: Bilişim Sistemleri")
print ("Hobi: Futbol")

#görev 2
print((9.5*4.5-2.5*3) / (45.5-3.5))

#görev 3
#6 terimle hesap
pi_6 = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
print(pi_6)
#7 terimle hesap
pi_7 = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13)
print(pi_7)

# görev 4
# A kısmındaki hata sözdizimi yani print("merhaba dünya) kısmında tırnak kapatılmamıştır doğrusu budur  print("merhaba dünya")
# B kısmındaki hata çalışma zamanı yani print(10/0) kısmında matematikte 0'a sayı bölünemez doğrusu budur  print(10/1) vb.
# C kısmındaki hata mantık yani print(3+5/2) kısmında işlem önceliği baz alınmamıştır doğrusu budur  print((3+5)/2)

#görev 5
import turtle
t=turtle.Turtle()
t.speed(3)
#kare çizimi
for_in range(4)
    t.forward(100)
    t.left(90)
#üçgen çizimi
# karenin sol üstüne çıktım
    t.forward(100)
    t.left(90)
    t.right(90)
#çatı üçgenenini çiziyorum
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
#isim yazma
t.penup()
t.goto(130, 40)
t.pendown()
t.write ("yusuf arslan", font=("Arial", 14, "normal"))

turtle.done()
