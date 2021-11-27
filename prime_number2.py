n = int(input("lütfen sayı giriniz : "))
liste = [2,3,5,7]
for i in range(2, n+1):
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        liste.append(i)
print(liste)







n = int(input("lütfen sayı giriniz : "))
lst = []
for i in range(2, n+1):
    sayac = 0
    for j in range(2,i):
        if i % j == 0:
            sayac += 1
    if sayac == 0:
        lst.append(i)
print(lst)


