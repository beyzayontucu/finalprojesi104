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

        #Verileri içeren data isimli sözlük oluşturulur. Burada get ile fonksiyon çağırma işlemi uygulandı.
        #Sözlüğün anahtarları ve değerleri girildi.
        data = {
            "Nesne": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
            "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
            "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
            "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
            "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
            "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
            "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
            "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
            "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
            "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
            "Yıpranma Payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0, 0],
            "Teşvik Primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
            "Yeni Maaş": [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(), mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas()]
        }

        #Sözlük kullanarak DataFrame oluşturma. Bu kod sayesinde veriler tablo şeklinde görünür.
        df = pd.DataFrame(data)  # DataFrame df adıyla bir değişkene atar.
        print(df)

        #Bazı değişken değerlerini boş oluşturabilmek amacıyla DataFrame için bu değerler 0 atanır.
        df = df.fillna(0)

        #Tecrube sütununundaki verileri yıla çevirmek için.
        df['Tecrübe'] = df['Tecrübe'] // 12  # Öznitelik olarak kullanım

        #Çalışan, mavi yaka ve beyaz yaka için tecrübe ve yeni maaş ortalamalarını her grup için hesaplamak ve yazdırmak için.
        grouped = df.groupby("Nesne").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})  # Nesne sütünuna göre gruplama yapar.
        print(grouped)

        #Maaşı 15000TL üzerinde olanların toplam sayısını bulmak için.
        maas_fazla_15000 = df[df["Maaş"] > 15000]  # Burada maaşı 15000'in üzerindekilerin sayısını bulur.
        toplam_sayi = len(maas_fazla_15000)  # toplam_sayi değişkenine atar.
        print("Maaşı 15000TL üzerinde olanların toplam sayısı:", toplam_sayi)

        #Yeni maaşa göre DataFrame'i küçükten büyüğe sıralar, df_sirali adlı bir DataFrame'e atar ve yazdırır.
        df_sirali = df.sort_values("Yeni Maaş")
        print(df_sirali)

        #Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulmak ve yazdırmak için.
        beyazyaka_tecrube_ust_3 = df[(df["Nesne"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)]
        print(beyazyaka_tecrube_ust_3)

        #Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek göstermek ve yazdırmak için.
        yeni_maas_ust_10000 = df[(df["Yeni Maaş"] > 10000)].iloc[2:4, [1, 12]]
        print(yeni_maas_ust_10000)

        #Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturmak ve yazdırmak için.
        yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
        print(yeni_df)


    except Exception as e:
        print("Hata:", str(e))  #Hata olması durumunda Hata mesajını verir.

if __name__ == "__main__": #Bu ifade Python'da bir komutun doğrudan çalıştırılıp çalıştırılmadığını kontrol etmek için kullanılır.
    main() #Komutu çalıştırırken o komutu __name__ adında bir değişkene atar. Eğer komut doğrudan çalıştırılıyorsa, __name__ değişkenine "__main__" değeri atanır.