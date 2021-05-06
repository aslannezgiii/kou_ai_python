"""
Kullanıcıdan alacağınız 5 tane sayının asal olup olmadığını kontrol edip, her bir sayı için
ekrana sayı asalsa asal, asal değilse asal değil yazdırın.
"""

input_sayisi = 1;
sayilar = []

while input_sayisi <= 5: #5 sayı alınacak
    number =int(input("{}. sayıyı giriniz".format(input_sayisi)))
    input_sayisi = input_sayisi + 1
    sayilar.append(number)

print(sayilar) #kontrol edildi

for eleman in sayilar:
    if eleman > 1:
        for j in range(2,eleman):
            if (eleman % j) == 0:
                print("{} sayısı asal değildir".format(eleman))
                break
        else:
            print("{} sayısı asaldır".format(eleman))
