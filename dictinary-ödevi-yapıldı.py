cümle = input("lütfen cümle giriniz:")
yeni_cümlemiz = tuple(cümle)
yeni_dict = { }
for i in yeni_cümlemiz:
    yeni_dict[i] = yeni_cümlemiz.count(i)
print(yeni_dict)
