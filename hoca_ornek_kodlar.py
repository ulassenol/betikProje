import sqlite3
baglanti=sqlite3.connect('deneme.sqlite')
isaretci=baglanti.cursor()

isaretci.execute("""CREATE TABLE ogrenciler(kayitno 
INTEGER PRIMARY KEY, ogrencino INTEGER NOT NULL, adi 
VARCHAR(50), soyadi VARCHAR(50), cinsiyeti VARCHAR(1))""")


isaretci.execute("""INSERT INTO ogrenciler(ogrencino, adi, soyadi, cinsiyeti) VALUES(1,'Mehmet', 'ŞİMŞEK', 'E')""")
isaretci.execute("""INSERT INTO ogrenciler(ogrencino, adi, soyadi, cinsiyeti) VALUES(55,'Ali', 'AK', 'E')""")

baglanti.commit()

def hepsi():
	dataset = isaretci.execute('''select * from ogrenciler;''')
	print(dataset.fetchall())
	

def arama():
	girilen=input("Aranan ismi giriniz: ")
	dataset = isaretci.execute('''select * from ogrenciler 
	WHERE adi='''+ "'"+ girilen+ "'")
	print(dataset.fetchall())

def arama_alternatif():
	ad=input("Aranan ismi giriniz: ")
	dataset = isaretci.execute("SELECT * FROM ogrenciler WHERE adi = '%s'" % ad)
	
	for i in dataset.fetchall():
		print("Kayıt No:\t",i[0])
		print("Öğrenci No:\t",i[1])
		print("Adı:\t\t",i[2])
		print("Soyadı:\t\t",i[3])
		print("Cinsiyeti:\t",i[4])
	
def cok_parametreli_arama():
	ad=input("İsim girin: ")
	soyad=input("Soyisim girin: ")
	dataset = isaretci.execute("SELECT * FROM ogrenciler WHERE adi = ? AND soyadi = ?", (ad, soyad));
	
	for i in dataset.fetchall():
		print("----------------------")
		print("Kayıt No: %d\nNumarası: %d\nAdı: %s\nSoyadi: %s\nCinsiyeti: %s" %i)


def ekleme():
	no=input("Numara girin: ")
	ad=input("İsim girin: ")
	soyad=input("Soyisim girin: ")
	cinsiyet=input("Cinsiyet girin: ")
	isaretci.execute('''INSERT INTO ogrenciler(ogrencino, adi, 
	soyadi, cinsiyeti) VALUES(?,?,?,?)''',(no,ad,soyad,cinsiyet))
	baglanti.commit()

def guncelleme():
	ad=input("İsim girin: ")
	soyad=input("Soyisim girin: ")
	numara=input("Yeni numarayı girin: ")
	dataset = isaretci.execute("""UPDATE ogrenciler SET ogrencino=? WHERE adi = ? AND soyadi = ?", (numara, ad, soyad)""");
	baglanti.commit()
	dataset = isaretci.execute("SELECT * FROM ogrenciler WHERE adi = ? AND soyadi = ?", (ad, soyad));
	for i in dataset.fetchall():
		print("----------------------")
		print("Kayıt No: %d\nNumarası: %d\nAdı: %s\nSoyadi: %s\nCinsiyeti: %s" %i)
ekleme()
hepsi()
guncelleme()

arama()
arama_alternatif()
cok_parametreli_arama()	
