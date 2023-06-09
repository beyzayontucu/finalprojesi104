from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) #Belirtilen değerleri Calisan sınıfından miras alır.
        self.__yipranma_payi = yipranma_payi #Private olarak değişken bulunur.

    def get_yipranma_payi(self): #yipranma_payi değerini döndürür.
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi): #yipranma_payi değerini güncellemek için kullanılır.
        self.__yipranma_payi = yipranma_payi

    def get_yeni_maas(self): #yeni_maas değerini döndürür.
        zam_orani = self.zam_hakki() #zam_orani değişkenine mevcut maaşın zam_hakki fonksiyonuna göre hesaplanan zam oranını atar.
        yeni_maas = self.get_maas() + zam_orani #yeni_maas değişkenine mevcut maaşa zam_orani'ni ekleyerek yeni maaşı hesaplar.
        if yeni_maas == self.get_maas(): #eğer yeni_maas mevcut maaşa eşitse mevcut maaşı döndürür.
            return self.get_maas()
        else:
            return yeni_maas #Eğer bir zam yapılmışsa, yeni maaşı döndürür.

    def __statu_bul(self):
        return "Mavi Yaka" #__statu_bul metodu çağrıldığında "Mavi Yaka" değeri döndürür.

    def zam_hakki(self):
        try:  # try içinde kontrol ediliyor.
            if self.get_tecrube() <= 24: #Eğer tecrübe ayı 24 veya daha az ise, yipranma_payi değerini 10 ile çarparak sonucu döndürür.
                return self.__yipranma_payi * 10
            elif 24 < self.get_tecrube() <= 48 and self.get_maas() < 15000: #Eğer tecrübe ayı 24'ten büyük ve 48'e eşit veya küçük,maaşı 15000'den küçükse maaşın tecrübe değerine göre modunu alır,bu değeri 2'ye böler.Bu değeri yipranma_payi değerinin 10 katı ile toplayıp sonucu döndürür.
                return (self.get_maas() % self.get_tecrube() / 2) + (self.__yipranma_payi * 10)
            elif self.get_tecrube() > 48 and self.get_maas() < 25000: #Eğer tecrübe ayı 48'den büyük, maaşı 25000'den küçükse maaşın tecrübe değerine göre modunu alır (maas % tecrube) ve bu değeri 3'e böler.Bu değeri yipranma_payi değerinin 10 katı ile toplayıp sonucu döndürür.
                return (self.get_maas() % self.get_tecrube() / 3) + (self.__yipranma_payi * 10)
            else:
                return 0 #Eğer yukarıdaki koşullar sağlanmazsa zam hakkı olarak 0 değeri döndürülür.
        except Exception as e:
            print(f"Hesaplarken Hata Oluştu: {e}")  # Hata olması durumunda hata mesajını verir.

    def __str__(self): #__str__ ile ilgili verileri yazdırır.
        return super().__str__() + f"\nYıpranma Payı: {float(self.__yipranma_payi)} TL"

if __name__ == "__main__":
    try:  # try içinde kontrol ediliyor.
        mavi_yaka1 = MaviYaka("78901234567", "Aral", "Kara", 32, "Erkek", "Türk", "İnşaat", 40, 5000, 0.2)
        print(mavi_yaka1)
        mavi_yaka2 = MaviYaka("89012345678", "Sinem", "Aydın", 27, "Kadın", "Türk", "Diğer", 33, 8000, 0.3)
        print(mavi_yaka2)
        mavi_yaka3 = MaviYaka("90123456789", "Deniz", "Arslan", 35, "Erkek", "Türk", "Diğer", 60, 2000, 0.4)
        print(mavi_yaka3)

    except Exception as e:
        print("Hata:", str(e))  # Hata olması durumunda Hata mesajını verir.