from Insanlar import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #Belirtilen değerleri Insan sınıfından miras alır.
        self.__tecrubeler = tecrubeler #Private olarak değişken bulunur.

    def get_tecrubeler(self): #tecrubeler değerini döndürür.
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler): #tecrubeler değerini güncellemek için kullanılır.
        self.__tecrubeler = tecrubeler

    def __statu_bul(self): #statu_bul fonksiyonu.
        etkiler = { #etkiler adında sözlük tanımlanır ve statu ile etkiye ilişkin eşleme sağlar.
            "Mavi Yaka": 0.20, #statüde mavi yaka için tecrübe değerinin %20 sini hesaplar.
            "Beyaz Yaka": 0.35, #statüde beyaz yaka için tecrübe değerinin %35 sini hesaplar.
            "Yönetici": 0.45 #statüde yönetici için tecrübe değerinin %45 sini hesaplar.
        }

        max_etki = max(self.__tecrubeler.values(), default=0) #__tecrubeler'deki en yüksek etki değerini tutmak için. Eğer sözlük boşsa 0 değeri kullanılır.
        for statu, yil in self.__tecrubeler.items(): #for döngüsüyle self.__tecrubeler sözlüğünü dolaşır ve en yüksek etkiye sahip olan statüyü bulur.
            if yil == max_etki: #yil=max_etki olup olmadığını sorgular.
                return statu #Eşleşen statüyü döndürerek, en yüksek etkiye sahip olan statünün adını elde eder.

        return "" #Eğer self.__tecrubeler sözlüğü boş ise veya en yüksek etkiye sahip bir statü bulunamazsa, boş bir dize ("") döndürür.

    def statu_bul(self): #__statu_bul() metotunu çağırmaktadır.
        return self.__statu_bul() #__statu_bul() metodunu çağırarak en yüksek etkiye sahip olan statünün adını döndürür.

    def __str__(self): #__str__ ile ilgili verileri yazdırır.
        return super().__str__() + f"\nYıl Bazında Tecrübeler: {self.__tecrubeler}\nEn Uygun Statü: {self.statu_bul()}"

if __name__ == "__main__":
    try:  # try içinde kontrol ediliyor.
        issiz1 = Issiz("12345678935", "Ali", "Yılmaz", 30, "Erkek", "Türk",  {"mavi yaka": 2, "beyaz yaka": 5, "yönetici": 0})
        print(issiz1)
        issiz2 = Issiz("98765432113", "Ayşe", "Demir", 25, "Kadın", "Türk", {"mavi yaka": 7, "beyaz yaka": 6, "yönetici": 2})
        print(issiz1)
        issiz3 = Issiz("56789012304", "Mehmet", "Kaya", 40, "Erkek", "Türk", {"mavi yaka": 1, "beyaz yaka": 4, "yönetici": 6})
        print(issiz1)

    except Exception as e:
        print("Hata:", str(e))  # Hata olması durumunda Hata mesajını verir.
