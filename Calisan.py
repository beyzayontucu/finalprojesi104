from Insanlar import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #Belirtilen değerleri Insan sınıfından miras alır.
        self.__sektor = sektor #Private olarak değişken bulunur.
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = 0

    def get_sektor(self): #sektor değerini döndürür.
        return self.__sektor

    def set_sektor(self, sektor): #sektor değerini güncellemek için kullanılır.
        self.__sektor = sektor

    def get_tecrube(self): #tecrube değerini döndürür.
        return self.__tecrube

    def set_tecrube(self, tecrube): #tecrube değerini güncellemek için kullanılır.
        self.__tecrube = tecrube

    def get_maas(self): #maas değerini döndürür.
        return self.__maas

    def set_maas(self, maas): #maas değerini güncellemek için kullanılır.
        self.__maas = maas

    def get_yeni_maas(self):
        zam_orani = self.zam_hakki() # zam_orani değişkenine mevcut maaşın zam_hakki fonksiyonuna göre hesaplanan zam oranını atar.
        return self.__maas + zam_orani # yeni_maas değişkenine mevcut maaşa zam_orani'ni ekleyerek yeni maaşı hesaplar.


    def zam_hakki(self): #zam_hakki'nı hesaplayan fonksiyon.
        try:  # try içinde kontrol ediliyor.
            if self.__tecrube < 2: #Eğer tecrube 24 aydan küçükse, zam hakkı olarak 0 değeri döndürülür.
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000: #Eğer tecrube 24 ve 48 aydan küçük eşitse ve maaş 15000'den küçükse, zam hakkı olarak maaşın tecrubeye bölümünden kalan değer döndürülür.
                return self.__maas * (self.__tecrube / 100)
            elif self.__tecrube > 4 and self.__maas < 25000: #Eğer tecrube 48 aydan büyük ve maaş 25000'den küçükse, zam hakkı olarak maaşın tecrubeye bölümünden kalan değerin yarısı döndürülür.
                return (self.__maas * self.__tecrube) / 200
        except Exception as e:
            print(f"Hesaplarken Hata Oluştu: {e}")  # Hata olması durumunda hata mesajını verir.


    def __str__(self): #__str__ ile ilgili verileri yazdırır.
        return super().__str__() + f"\nSektör: {self.__sektor}\nTecrübe: {self.__tecrube} ay\nMaaş: {float(self.__maas)}\nYeni Maaş : {float(self.get_yeni_maas())} TL"


if __name__ == "__main__":
    try:  # try içinde kontrol ediliyor.
        calisan1 = Calisan("56789012321", "Ahmet", "Öztürk", 35, "Erkek", "Türk", "Muhasebe", 8, 10000)
        print(calisan1)
        calisan2 = Calisan("45678901298", "Didem", "Koç", 28, "Kadın", "Türk", "İnşaat", 60, 18000)
        print(calisan2)
        calisan3 = Calisan("23456789055", "Bora", "Aydemir", 45, "Erkek", "Türk", "Teknoloji", 30, 9000)
        print(calisan3)

    except Exception as e:
        print("Hata:", str(e))  # Hata olması durumunda Hata mesajını verir.
