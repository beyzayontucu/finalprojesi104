class Insan:  #Insan sınıfı oluşturma.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk): #__init__ ile insan nesnesi için kullanılacak başlangıç değeri alır ve değer alanlarına atar.
        self.__tc_no = tc_no  #Private olarak değişken bulunur.
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def get_tc_no(self): #tc_no değerini döndürür.
        return self.__tc_no

    def set_tc_no(self, tc_no): #tc_no değerini güncellemek için kullanılır.
        self.__tc_no = tc_no

    def get_ad(self): #ad değerini döndürür.
        return self.__ad

    def set_ad(self, ad): #ad değerini güncellemek için kullanılır.
        self.__ad = ad

    def get_soyad(self): #soyad değerini döndürür.
        return self.__soyad

    def set_soyad(self, soyad): #soyad değerini güncellemek için kullanılır.
        self.__soyad = soyad

    def get_yas(self): #yas değerini döndürür.
        return self.__yas

    def set_yas(self, yas): #yas değerini güncellemek için kullanılır.
        self.__yas = yas

    def get_cinsiyet(self): #cinsiyet değerini döndürür.
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet): #cinsiyet değerini güncellemek için kullanılır.
        self.__cinsiyet = cinsiyet

    def get_uyruk(self): #uyruk değerini döndürür.
        return self.__uyruk

    def set_uyruk(self, uyruk): #uyruk değerini güncellemek için kullanılır.
        self.__uyruk = uyruk

    def __statu_bul(self): #Sınıfın içindeki __statu_bul adlı bir metot bulunur ama bu metotun içi boştur (pass).
        pass

    def __str__(self): #__str__ ile ilgili verileri yazdırır.
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"
