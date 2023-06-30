print(15 /4)

# bölüm sonucunu int e dönüştürürsem sadece tam sayı kısmını verecektir.
print(int(15 / 4))
# round sayıyı yuvarlamamıza yardımcı olur.
print(round(15 / 4))

#virgülden sonra kaç basamağı yuvarlayacağımızı belirterek de kullanabiliriz.
print(round(1.899999,2))

# iki tane // işareti kullanarak yaptığımız işlemde sonuç yine tam sayı olarak çıkar.
print(15 // 4)

print(type(15 // 4))

result = 12 / 3
result /= 4
print(result)