import os
# sqlite3'ı projeye eklendi
import sqlite3 as sql

# global degiskenler
veritabaniAdi = 'dershane.sqlite'

def veritabaniAdiGetir():
    return veritabaniAdi 

def veritabaniOlustur(veritabaniAdi):
    # veritabanının adını ekleyerek bağlantıyı oluşturdu
    global baglanti
    baglanti = sql.connect(veritabaniAdi)
    global imlec
    # veritabanında işlem yapabilmek için imleç oluşturdu
    imlec = baglanti.cursor()

def tablolariOlustur():
    # imlecin metodunu kullanarak Yonetici tablosunu oluşturdu
    imlec.execute("""CREATE TABLE IF NOT EXISTS Yonetici (
                    yoneticiID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tcNo INTEGER,
                    ad TEXT,
                    soyad TEXT,
                    cinsiyet TEXT,
                    eposta TEXT,
                    durum TEXT)""")
    # imlecin metodunu kullanarak Ogrenci tablosunu oluşturdu
    imlec.execute("""CREATE TABLE IF NOT EXISTS Ogrenci (
                    ogrenciID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    tcNo INTEGER UNIQUE,
                    ad TEXT,
                    soyad TEXT,
                    cinsiyet TEXT,
                    eposta TEXT,
                    durum TEXT)""")
    # imlecin metodunu kullanarak Portal tablosunu oluşturdu
    imlec.execute("""CREATE TABLE IF NOT EXISTS Portal (
                    portalID INTEGER PRIMARY KEY AUTOINCREMENT,
                    kullaniciID INTEGER,
                    kullaniciAdi TEXT,
                    sifre TEXT,
                    yetki TEXT)""")
    # imlecin metodunu kullanarak SinavSonuc tablosunu oluşturdu
    imlec.execute("""CREATE TABLE IF NOT EXISTS SinavSonuc (
                    sinavSonucID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ogrenciID INTEGER,
                    sinavID INTEGER,
                    dogru TEXT,
                    yanlis TEXT, 
                    bos TEXT)""")

def yoneticiEkle():
    tcNo = input('T.C. Numarası\t: ')
    ad = input('Adı\t\t: ')
    soyad = input('Soyadı\t\t: ')
    cinsiyet = input('Cinsiyeti\t: ')
    eposta = input('E-Posta Adresi\t: ')
    durum = input('Durumu\t\t: ')
    imlec.execute("""INSERT INTO 
                        Yonetici 
                    VALUES (
                        NULL, ?, ?, ?, ?, ?, ?)""", (tcNo, ad, soyad, cinsiyet, eposta, durum))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuEkle()
    
def ogrenciEkle():
    tcNo = input('T.C. Numarası\t: ')
    ad = input('Adı\t\t: ')
    soyad = input('Soyadı\t\t: ')
    cinsiyet = input('Cinsiyeti\t: ')
    eposta = input('E-Posta Adresi\t: ')
    durum = input('Durumu\\tt: ')
    imlec.execute("""INSERT INTO 
                        Ogrenci 
                    VALUES (
                        NULL, ?, ?, ?, ?, ?, ?)""", (tcNo, ad, soyad, cinsiyet, eposta, durum))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuEkle()
    
def portalEkle():
    kullaniciID = input("Kullanıcının ID'si\t: ")
    kullaniciAdi = input('Kullanıcı Adı\t: ')
    sifre = input('Şifresi\t\t: ')
    yetki = input('Yetkisi\t: ')
    imlec.execute("""INSERT INTO 
                        Portal 
                    VALUES (
                        NULL, ?, ?, ?, ?)""", (kullaniciID, kullaniciAdi, sifre, yetki))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuEkle()
    
def sinavSonucuEkle():
    ogrenciID = input("Öğrencinin ID'si\t: ")
    sinavID = input("Sınavın ID'si\t: ")
    dogru = input('Doğru Sayısı\t: ')
    yanlis = input('Yanlış Sayısı\t: ')
    bos = input('Boş Sayısı\t: ')
    imlec.execute("""INSERT INTO 
                        SinavSonuc 
                    VALUES (
                        NULL, ?, ?, ?, ?, ?)""", (ogrenciID, sinavID, dogru, yanlis, bos))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuEkle()
    
def yoneticiGuncelle():
    yoneticileriGoster()
    secim = input("Güncellemek istediğiniz yöneticinin ID'sini girin : ")
    ekraniTemizle()
    yoneticiAraID(secim)
    tcNo = input('T.C. Numarası\t: ')
    ad = input('Adı\t\t: ')
    soyad = input('Soyadı\t\t: ')
    cinsiyet = input('Cinsiyeti\t: ')
    eposta = input('E-Posta Adresi\t: ')
    durum = input('Durumu\t\t: ')
    imlec.execute("""UPDATE 
                        Yonetici 
                    SET 
                        tcNo = ?, 
                        ad = ?, 
                        soyad = ?, 
                        cinsiyet = ?, 
                        eposta = ?, 
                        durum = ?
                    WHERE
                        yoneticiID = ?""", (tcNo, ad, soyad, cinsiyet, eposta, durum, secim))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuGuncelle()
    
def ogrenciGuncelle():
    ogrencileriGoster()
    secim = input("Güncellemek istediğiniz öğrencinin ID'sini girin : ")
    ekraniTemizle()
    ogrenciAraID(secim)
    tcNo = input('T.C. Numarası\t: ')
    ad = input('Adı\t\t: ')
    soyad = input('Soyadı\t\t: ')
    cinsiyet = input('Cinsiyeti\t: ')
    eposta = input('E-Posta Adresi\t: ')
    durum = input('Durumu\t\t: ')
    imlec.execute("""UPDATE 
                        Ogrenci 
                    SET 
                        tcNo = ?, 
                        ad = ?, 
                        soyad = ?, 
                        cinsiyet = ?, 
                        eposta = ?, 
                        durum = ?
                    WHERE
                        ogrenciID = ?""", (tcNo, ad, soyad, cinsiyet, eposta, durum, secim))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuGuncelle()
    
def portalGuncelle():
    portallariGoster()
    secim = input("Güncellemek istediğiniz portalın ID'sini girin : ")
    ekraniTemizle()
    portalAraID(secim)
    kullaniciID = input('Kullanıcı ID\t: ')
    kullaniciAdi = input('Kullanıcı Adı\t: ')
    sifre = input('Şifre\t\t: ')
    yetki = input('Yetki\t\t: ')
    imlec.execute("""UPDATE 
                        Portal 
                    SET 
                        kullaniciID = ?, 
                        kullaniciAdi = ?, 
                        sifre = ?, 
                        yetki = ?
                    WHERE
                        portalID = ?""", (kullaniciID, kullaniciAdi, sifre, yetki, secim))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuGuncelle()
    
def sinavSonucuGuncelle():
    sinavSonuclariniGoster()
    secim = input("Güncellemek istediğiniz sınavın sonucun ID'sini girin : ")
    ekraniTemizle()
    portalAraID(secim)
    ogrenciID = input('Öğrenci ID\t: ')
    sinavID = input("Sınavın ID\t: ")
    dogru = input('Doğru Sayısı\t: ')
    yanlis = input('Yanlış Sayısı\t: ')
    bos = input('Boş Sayısı\t: ')
    imlec.execute("""UPDATE 
                        SinavSonuc 
                    SET 
                        kullaniciID = ?, 
                        kullaniciAdi = ?, 
                        sifre = ?, 
                        yetki = ?
                    WHERE
                        sinavSonucID = ?""", (ogrenciID, sinavID, dogru, yanlis, bos, secim))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuGuncelle()

def ogrenciSil():
    ogrencileriGoster()
    secim = input("Silmek istediğiniz öğrencinin ID'sini girin : ")
    ekraniTemizle()
    imlec.execute("""DELETE FROM
                        Ogrenci 
                    WHERE
                        ogrenciID = ?""", (secim))
    # yapılan değişiklikleri tabloya yansıtmak için baglantinin metodunu kullandı
    baglanti.commit()
    yoneticiMenuSil()


def yoneticiAraID(yoneticiID):
    imlec.execute("""SELECT
                        *
                    FROM
                        Yonetici
                    WHERE
                        yoneticiID = ? """, (yoneticiID))
    print(imlec.fetchone())

def ogrenciAraID(ogrenciID):
    imlec.execute("""SELECT
                        *
                    FROM
                        Ogrenci
                    WHERE
                        ogrenciID = ? """, (ogrenciID))
    print(imlec.fetchone())

def portalAraID(portalID):
    imlec.execute("""SELECT
                        *
                    FROM
                        Portal
                    WHERE
                        portalID = ? """, (portalID))
    print(imlec.fetchone())

def sinavSonucID(sinavSonucID):
    imlec.execute("""SELECT
                        *
                    FROM
                        SinavSonuc
                    WHERE
                        sinavSonucID = ? """, (sinavSonucID))
    print(imlec.fetchone())

def yoneticileriGoster():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        Yonetici""")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)

def ogrencileriGoster():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        Ogrenci""")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)

def ogrencileriGosterDurum():
    durum = input('Durum (aktif/pasif)\t: ')
    imlec.execute("SELECT * From Ogrenci WHERE durum = " + "'" + durum + "'")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)
        
def ogrencileriGosterCinsiyet():
    cinsiyet = input('Cinsiyet (Erkek/Kadın)\t: ')
    imlec.execute("SELECT * From Ogrenci WHERE cinsiyet = " + "'" + cinsiyet + "'")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)
        
def portallariGoster():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        Portal""")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)
        
def sinavSonuclariniGoster():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        SinavSonuc""")
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)

def ogrenciMenuSinavSonucu():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        SinavSonuc
                    WHERE
                        ogrenciID = ?""", (ogrenciID))
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)

def girisEkrani():
    ekraniTemizle()
    global kullaniciAdi, sifre, yetki
    print('Sisteme girebilmek için yetkili girişi yapmalısınız...')
    kullaniciAdi = input('Kullanıcı Adı\t: ')
    sifre = input('Şifre\t\t: ')
    yetki = input('Yetki\t\t: ')
    yetkiKontrol()
    
def yetkiKontrol():
    imlec.execute("""SELECT 
                        * 
                    FROM 
                        Portal 
                    WHERE 
                        kullaniciAdi = ? 
                        AND 
                        sifre = ? 
                        AND 
                        yetki = ? """, (kullaniciAdi, sifre, yetki))
    veriVarMi = imlec.fetchone()
    if veriVarMi:
        if yetki == 'yonetici':
            yoneticiMenu()
        elif yetki == 'ogrenci':
            ogrenciMenu()
    else:
        girisEkrani()

def cikis():
    quit()

def yoneticiMenuEkle():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Yönetici Ekle')
    print('\t2- Öğrenci Ekle')
    print('\t3- Portal Ekle')
    print('\t4- Sınav Sonucu Ekle')
    print('\t5- GERİ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        yoneticiEkle()
    elif secim == '2':
        ogrenciEkle()
    elif secim == '3':
        portalEkle()
    elif secim == '4':
        sinavSonucuEkle()
    elif secim == '5':
        yoneticiMenu()
    else:
        yoneticiMenuEkle()

def yoneticiMenuGuncelle():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Yönetici Güncelle')
    print('\t2- Öğrenci Güncelle')
    print('\t3- Portal Güncelle')
    print('\t4- Sınav Sonucu Güncelle')
    print('\t5- GERİ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        yoneticiGuncelle()
    elif secim == '2':
        ogrenciGuncelle()
    elif secim == '3':
        portalGuncelle()
    elif secim == '4':
        sinavSonucuGuncelle()
    elif secim == '5':
        yoneticiMenu()
    else:
        yoneticiMenuGuncelle()

def yoneticiMenuSil():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Yönetici Sil')
    print('\t2- Öğrenci Sil')
    print('\t3- Portal Sil')
    print('\t4- Sınav Sonucu Sil')
    print('\t5- GERİ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        yoneticiSil()
    elif secim == '2':
        ogrenciSil()
    elif secim == '3':
        portalSil()
    elif secim == '4':
        sinavSonucSil()
    elif secim == '5':
        yoneticiMenu()
    else:
        yoneticiMenuSil()

def yoneticiMenuAra():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Yöneticilerde Ara')
    print('\t2- Öğrencilerde Ara')
    print('\t3- Portallarda Ara')
    print('\t4- Sınav Sonuçlarında Ara')
    print('\t5- GERİ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        yoneticiMenuAraYonetici()
    elif secim == '2':
        yoneticiMenuAraOgrenci()
    elif secim == '3':
        yoneticiMenuAraPortal()
    elif secim == '4':
        yoneticiMenuAraSinavSonucu()
    elif secim == '5':
        yoneticiMenu()
    else:
        yoneticiMenuAra()

def yoneticiMenuAraOgrenci():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Tümünü Göster')
    print('\t2- Duruma Göre Göster')
    print('\t3- Cinsiyete Göre')
    print('\t4- GERİ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        ogrencileriGoster()
    elif secim == '2':
        ogrencileriGosterDurum()
    elif secim == '3':
        ogrencileriGosterCinsiyet()
    elif secim == '4':
        yoneticiMenuAra()
    else:
        yoneticiMenuAraOgrenci()

def yoneticiMenu():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- EKLE')
    print('\t2- GÜNCELLE')
    print('\t3- SİL')
    print('\t4- ARA')
    print('\t5- ÇIKIŞ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        yoneticiMenuEkle()
    elif secim == '2':
        yoneticiMenuGuncelle()
    elif secim == '3':
        yoneticiMenuSil()
    elif secim == '4':
        yoneticiMenuAra()
    elif secim == '5':
        cikis()
    else:
        yoneticiMenu()

def ogrenciMenu():
    ekraniTemizle()
    print('-' * 30)
    print('\t1- Sinav Sonucu Göster')
    print('\t2- ÇIKIŞ')
    print('-' * 30)
    secim = input('Yapmak istediğiniz işlemin numarasını girin : ')
    if secim == '1':
        ogrenciMenuSinavSonucu()
    elif secim == '2':
        cikis()
    else:
        yoneticiMenu()

def ekraniTemizle():
    os.system('CLS')




#baglanti.close()



veritabaniOlustur(veritabaniAdiGetir())
tablolariOlustur()
girisEkrani()         