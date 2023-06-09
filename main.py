import pandas as pd  #DataFrame oluşturmak için pandas kütüphanesi kullanıyor.
from Insanlar import Insan  #Insanlar modülünden Insan sınıfını içeri aktarıyor.
from Issiz import Issiz  #Issiz modülünden Issiz sınıfını içeri aktarıyor.
from Calisan import Calisan  #Calisan modülünden Calisan sınıfını içeri aktarıyor.
from BeyazYaka import BeyazYaka  #BeyazYaka modülünden BeyazYaka sınıfını içeri aktarıyor.
from MaviYaka import MaviYaka  #MaviYaka modülünden MaviYaka  sınıfını içeri aktarıyor.

def main():  #main fonksiyonunu tanımlar.
    try:  #try bloğuyla hata kontrolü sağlanır.

        #İnsan nesnelerini oluşturma işlemi.
        insan1 = Insan("34298756410", "Veli", "Karan", "29", "Erkek", "Türk")
        insan2 = Insan("17763529078", "Angela", "Smith", "46", "Kadın", "İngiliz")
        sonuc1 = insan1.__str__()  #__str__() ile her nesnenin bilgilerini metin formatında alır.
        sonuc2 = insan2.__str__()
        print(sonuc1)  #Oluşturulan metinleri ekrana yazdırır.
        print()
        print(sonuc2)
        print()

        #İşsiz nesnelerini oluşturma işlemi.
        issiz1 = Issiz("12345678935", "Ali", "Yılmaz", 30, "Erkek", "Türk",  {"mavi yaka": 2, "beyaz yaka": 5, "yönetici": 0})
        issiz2 = Issiz("98765432113", "Ayşe", "Demir", 25, "Kadın", "Türk", {"mavi yaka": 7, "beyaz yaka": 6, "yönetici": 2})
        issiz3 = Issiz("56789012304", "Mehmet", "Kaya", 40, "Erkek", "Türk", {"mavi yaka": 1, "beyaz yaka": 4, "yönetici": 6})
        sonuc3 = issiz1.__str__()
        sonuc4 = issiz2.__str__()
        sonuc5 = issiz3.__str__()
        print(sonuc3)
        print()
        print(sonuc4)
        print()
        print(sonuc5)
        print()

        #Çalışan nesnelerini oluşturma işlemi.
        calisan1 = Calisan("56789012321", "Ahmet", "Öztürk", 35, "Erkek", "Türk", "Muhasebe", 8, 10000)
        calisan2 = Calisan("45678901298", "Didem", "Koç", 28, "Kadın", "Türk", "İnşaat", 60, 18000)
        calisan3 = Calisan("23456789055", "Bora", "Aydemir", 45, "Erkek", "Türk", "Teknoloji", 30, 9000)
        sonuc6 = calisan1.__str__()
        sonuc7 = calisan2.__str__()
        sonuc8 = calisan3.__str__()
        print(sonuc6)
        print()
        print(sonuc7)
        print()
        print(sonuc8)
        print()

        #MaviYaka nesneleri oluşturma işlemi.
        mavi_yaka1 = MaviYaka("78901234567", "Aral", "Kara", 32, "Erkek", "Türk", "İnşaat", 40, 5000, 0.2)
        mavi_yaka2 = MaviYaka("89012345678", "Sinem", "Aydın", 27, "Kadın", "Türk", "Diğer", 33, 8000, 0.3)
        mavi_yaka3 = MaviYaka("90123456789", "Deniz", "Arslan", 35, "Erkek", "Türk", "Diğer", 60, 2000, 0.4)
        sonuc9 = mavi_yaka1.__str__()
        sonuc10 = mavi_yaka2.__str__()
        sonuc11 = mavi_yaka3.__str__()
        print(sonuc9)
        print()
        print(sonuc10)
        print()
        print(sonuc11)
        print()

        #BeyazYaka nesneleri oluşturma işlemi.
        beyaz_yaka1 = BeyazYaka("01234567890", "Selin", "Yıldız", 29, "Kadın", "Türk", "Teknoloji", 120, 14000, 1000)
        beyaz_yaka2 = BeyazYaka("12345678901", "Burak", "Şahin", 36, "Erkek", "Türk", "Muhasebe", 100, 18000, 2000)
        beyaz_yaka3 = BeyazYaka("23456789012", "Elif", "Özkan", 42, "Kadın", "Türk", "Teknoloji", 150, 28000, 3000)
        sonuc12 = beyaz_yaka1.__str__()
        sonuc13 = beyaz_yaka2.__str__()
        sonuc14 = beyaz_yaka3.__str__()
        print(sonuc12)
        print()
        print(sonuc13)
        print()
        print(sonuc14)
        print()
