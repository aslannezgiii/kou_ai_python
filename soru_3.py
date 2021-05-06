"""
Elimizdeki üç adet string içerisindeki rakamlar temizlenip (sadece harfler kalacak) temiz
halleri bir listede tutulacaktır. Temiz halde listede bulunan isimlerin hepsi yan yana bir
string değişkeninde birleştirilecek ve aralarında (-) işareti olacaktır
"""
def temiz_veri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"

    ilk_string_list= [*ilk_string] #listeye çevirdik
    ikinci_string_list= [*ikinci_string] #listeye çevirdik
    ucuncu_string_list= [*ucuncu_string] #listeye çevirdik
    #print(ilk_string_list)
    #print(ikinci_string_list)
    #print(ucuncu_string_list)
    a = ['-']
    liste =  ilk_string_list  + a + ikinci_string_list  + a + ucuncu_string_list

    print(liste) #kontrol

    sayi = [*range(0,10)]
    for eleman in liste:
        #print(eleman)
        for num in sayi: #rakamları döndürelim
            if eleman  == str(num): #rakamları bul
                print("{} sayısı çıkartılmalıdır".format(eleman))
                #print("deneme",num) #kontrol
                liste.remove(eleman) #rakam çıkar
            else:
                continue
    #print(liste)
    Birlesmis_deger =  " ".join(liste)

    return Birlesmis_deger



print(temiz_veri())
