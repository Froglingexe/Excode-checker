import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="facebook"
)

# Cursor oluştur
mycursor = mydb.cursor()

# Kullanıcıdan girdileri al
numara = input("Sorgulanacak kişinin +90 formatındaki Telefon numarası: ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = numara + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if numara:
        sql = f"SELECT * FROM facebook WHERE NUMARA = '{numara}'"
    elif numara:
        sql = f"SELECT * FROM facebook WHERE NUMARA = '{numara}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            numara = kayit[1]
            ad = kayit[2]
            soyad = kayit[3]
            email = kayit[4] 
            birthday = kayit[5]
            gender = kayit[6]
            locale = kayit[7]           
            hometown = kayit[8]           
            location = kayit[9]

            
            dosya.write(f"NUMARASI:{numara}, ADI:{ad}, SOYADI:{soyad}, EMAİLİ:{email}, DOĞUM GÜNÜ:{birthday}, CİNSİYETİ:{gender}"
                        f" UYRUĞU:{locale}, MEMLEKETİ:{hometown}, YAŞADIĞI ŞEHİR:{location}\n".encode())
            

            print(f"NUMARASI:{numara}, ADI:{ad}, SOYADI:{soyad}, EMAİLİ:{email}, DOĞUM GÜNÜ:{birthday}, CİNSİYETİ:{gender}"
                        f" UYRUĞU:{locale}, MEMLEKETİ:{hometown}, YAŞADIĞI ŞEHİR:{location}\n".encode())  

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
