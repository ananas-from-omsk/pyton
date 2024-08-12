form = input("")

if form == "круг":
    r = float(input(""))
    s = 3.14 * r ** 2
    print(s)
elif form == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a*b)
elif form == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
    print(s)
