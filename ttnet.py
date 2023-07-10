import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ttnet"
)

# Cursor oluştur
mycursor = mydb.cursor()

# Kullanıcıdan girdileri al
adsoyad = input("Sorgulanacak kişinin bilgilerini İSİM SOYİSİM formatında giriniz: ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = adsoyad + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if adsoyad:
        sql = f"SELECT * FROM ttnet WHERE ADSOYAD = '{adsoyad}'"
    elif adsoyad:
        sql = f"SELECT * FROM ttnet WHERE ADSOYAD = '{adsoyad}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            adsoyad = kayit[1]
            gsm = kayit[3]
            eposta = kayit[4]
            adres = kayit[5] 
            sehir = kayit[6]

            
            dosya.write(f"ADI SOYADI:{adsoyad}, GSM HATTI:{gsm}, EPOSTA ADRESİ:{eposta}, ADRESİ:{adres}, YAŞADIĞI ŞEHİR:{sehir}\n".encode())
            

            print(f"ADI SOYADI:{adsoyad}, GSM HATTI:{gsm}, EPOSTA ADRESİ:{eposta}, ADRESİ:{adres}, YAŞADIĞI ŞEHİR:{sehir}\n".encode())  

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
