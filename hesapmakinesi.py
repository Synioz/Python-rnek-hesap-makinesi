while True:
    star = input("Hoş geliniz yapmak istediğiniz işlemi seçiiniz hesap makinesi için 1 çıkmak için 2 yazın 1:  ")
    if star == "1":
        print("Hesap makinesine hoş geliniz")
        sayi1 = int(input("İşlem yapmak istediğiniz 1. sayıyı seçiniz:  "))
        sayi2 = int(input("İşlem yapmak istediğiniz 2. sayıyı seçiniz:  "))
        islem = input("""Yapacağınız işlemi seçiniz (Toplama için: 1
                            Çıkartma için: 2
                            Çarpma için: 3
                            Bölme için: 4 yazınız):  """)
        if islem == "1":
            print(sayi1 + sayi2, "İşlem başarı ile tamamlandı.")
            break
        elif islem == "2":
            print(sayi1 - sayi2, "İşlem başarı ile tamamlandı.")
            break
        elif islem == "3":
            print(sayi1 * sayi2, "İşlem başarı ile tamamlandı.")
            break
        elif islem == "4":
            if sayi2 != 0:
                print(sayi1 / sayi2, "İşlem başarı ile tamamlandı.")
                break
            else:
                print("Bir sayıyı 0'a bölemezsiniz.")
        else:
            print("Böyle bir işlem bulunmuyor")

    elif star == "2":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim.")