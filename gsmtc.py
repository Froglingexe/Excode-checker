import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="avea"
)

# Cursor oluştur
mycursor = mydb.cursor()


if mydb.is_connected():
    print("NOT: GSM Sorgunuzun çalışması için database klasörünüzün ve '.frm' dosyalarınızın adını avea olarak değiştirmeniz gerekmektedir")

# Kullanıcıdan girdileri al
gsm = input("GSM Numarasını giriniz: ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = gsm + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if gsm:
        sql = f"SELECT * FROM avea WHERE GSM = '{gsm}'"
    else:
        sql = f"SELECT * FROM avea WHERE GSM = '{gsm}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            tc = kayit[1]
            
            dosya.write(f"TC:{tc}, GSM:{gsm}\n".encode())
            

            print(f"TC:{tc}, GSM:{gsm}\n".encode())    

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)

# Bağlantıyı kapat
mydb.close()
