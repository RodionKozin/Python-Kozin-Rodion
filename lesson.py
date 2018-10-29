i=int(input("Введите число: "))
max=-1
while i > 10:
    d = i % 10
    i //= 10
    if d > max:
        max = d
print(max)
