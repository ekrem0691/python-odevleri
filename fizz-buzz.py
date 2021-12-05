n = int(input("lütfen bir sayı giriniz:"))
liste = []
for i in range(1, n+1):
    if i % 15 == 0:
        liste.append("fizzbuzz")
    elif i % 5 == 0:
        liste.append("buzz")
    elif i % 3 == 0:
        liste.append("fizz")
    else:
        liste.append(i)
print(liste)
