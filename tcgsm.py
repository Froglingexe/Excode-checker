import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="avea"
)

# Cursor oluştur
mycursor = db.cursor()


if db.is_connected():
    print("NOT: GSM Sorgunuzun çalışması için database klasörünüzün ve '.frm' dosyalarınızın adını avea olarak değiştirmeniz gerekmektedir.")

# Kullanıcıdan girdileri al
tc = input("TC Numarasını giriniz: ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = "gsm" + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if tc:
        sql = f"SELECT * FROM avea WHERE TC = '{tc}'"
    else:
        sql = f"SELECT * FROM avea WHERE TC = '{tc}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            gsm = kayit[2]
            
            dosya.write(f"GSM:{gsm}, TC:{tc}\n".encode())

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)

# Bağlantıyı kapat
db.close()
