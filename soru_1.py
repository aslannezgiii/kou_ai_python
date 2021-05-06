"""
Kullanıcıdan alacağınız bir sayının çift sayı olup olmadığını kontrol edip ekrana sayı
çiftse çift, çift değilse tek yazdırın. (Kullanıcıdan sayı almak için input fonksiyonuna
bakabilirsiniz :))
"""
number = input("sayı giriniz: ")
#print(type(number))
number = int(number)
#print(type(number))
if number % 2 == 0:
    print("{} sayısı çifttir".format(number))
else:
    print("{} sayı tektir".format(number))
