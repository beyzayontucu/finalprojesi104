from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) #Belirtilen değerleri Calisan sınıfından miras alır.
        self.__tesvik_primi = tesvik_primi #Private olarak değişken bulunur.

    def get_tesvik_primi(self): #tesvik_primi değerini döndürür.
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi): #tesvik_primi değerini güncellemek için kullanılır.
        self.__tesvik_primi = tesvik_primi

    def get_yeni_maas(self):
        zam_orani = self.get_maas() * self.zam_hakki()/100 #zam_oranina mevcut maaş + zam_hakki fonksiyonuna göre hesaplanan zam oranını/100 değerini atar.
        yeni_maas = self.get_maas() + zam_orani #yeni_maas değişkenine mevcut maaşa zam_orani'ni ekleyerek yeni maaşı hesaplar.
        if yeni_maas == self.get_maas(): #eğer yeni_maas mevcut maaşa eşitse mevcut maaşı döndürür.
            return self.get_maas()
        else:
            return yeni_maas #Eğer bir zam yapılmışsa, yeni maaşı döndürür.

    def __statu_bul(self):
        return "Beyaz Yaka" #__statu_bul metodu çağrıldığında "Beyaz Yaka" değeri döndürür.

    def zam_hakki(self):  #zam_hakki'nı hesaplayan fonksiyon.
        try:
            if self.get_tecrube() <= 24: #Eğer tecrube ay sayısı 24 veya daha az ise, zam hakkı olarak 0 değeri döndürülür.
                return 0
            elif 24 < self.get_tecrube() <= 48 and self.get_maas() < 15000: #Eğer tecrube ayı 24'ten büyük, 48'den küçük veya eşitse ve maaş 15000'den küçük ise zam hakkı olarak maaşın tecrubeye bölümünden kalan değerin beş katı ile bir tesvik primi eklenmiş değeri döndürülür.
                return (self.get_maas() % self.get_tecrube() * 5) + self.__tesvik_primi
            elif self.get_tecrube() > 48 and self.get_maas() < 25000: #Eğer tecrube ayı 48'den büyük ve maaş 25000'den küçük ise, zam hakkı olarak maaşın tecrubeye bölümünden kalan değerin dört katı ile bir tesvik primi eklenmiş değeri döndürülür.
                return (self.get_maas() % self.get_tecrube() * 4) + self.__tesvik_primi
            else:
                return 0 #Eğer yukarıdaki koşullar sağlanmazsa zam hakkı olarak 0 değeri döndürülür.
        except Exception as e:
            print(f"Hesaplarken Hata Oluştu: {e}")  # Hata olması durumunda hata mesajını verir.

    def __str__(self): #__str__ ile ilgili verileri yazdırır.
        return super().__str__() + f"\nTeşvik Primi: {self.__tesvik_primi} TL"

if __name__ == "__main__":
    try:  # try içinde kontrol ediliyor.
        beyaz_yaka1 = BeyazYaka("01234567890", "Selin", "Yıldız", 29, "Kadın", "Türk", "Teknoloji", 120, 14000, 1000)
        print(beyaz_yaka1)
        beyaz_yaka2 = BeyazYaka("12345678901", "Burak", "Şahin", 36, "Erkek", "Türk", "Muhasebe", 100, 18000, 2000)
        print(beyaz_yaka2)
        beyaz_yaka3 = BeyazYaka("23456789012", "Elif", "Özkan", 42, "Kadın", "Türk", "Teknoloji", 150, 28000, 3000)
        print(beyaz_yaka3)

    except Exception as e:
        print("Hata:", str(e))  # Hata olması durumunda Hata mesajını verir.
