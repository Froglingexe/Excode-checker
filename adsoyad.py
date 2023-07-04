import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="101m"
)

# Cursor oluştur
mycursor = mydb.cursor()

# Kullanıcıdan girdileri al
adi = input("Adı: ")
soyadi = input("Soyadı: ")
il = input("Nüfüs İl (Boş bırakabilirsiniz): ")
nufusil = input("Nufus İlçe (Boş bırakabilirsiniz): ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = adi + "_" + soyadi + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if il:
        sql = f"SELECT * FROM 101m WHERE ADI = '{adi}' AND SOYADI = '{soyadi}' AND NUFUSIL = '{il}'"
    elif nufusil:
        sql = f"SELECT * FROM 101m WHERE ADI = '{adi}' AND SOYADI = '{soyadi}' AND NUFUSIL = '{il} AND NUFUSILCE = '{nufusil}'"
    else:
        sql = f"SELECT * FROM 101m WHERE ADI = '{adi}' AND SOYADI = '{soyadi}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            tc = kayit[1]
            adi = kayit[2]
            soyadi = kayit[3]
            baba_adi = kayit[6]
            ana_adi = kayit[5]
            dogum_tarihi = kayit[4]
            nufus_il = kayit[7]
            nufus_ilce = kayit[8]
            uyruk = kayit[9]
            
            dosya.write(f"TC:{tc}, ADI:{adi}, SOYADI:{soyadi}, BABA ADI:{uyruk}, ANNE ADI:{nufus_il}, "
                        f"DOĞUM TARIHI:{dogum_tarihi}, NUFUS İL:{ana_adi}, NUFUS İLÇE:{baba_adi}, ANNE TC:{nufus_ilce}\n".encode())
            

            print(f"TC:{tc}, ADI:{adi}, SOYADI:{soyadi}, BABA ADI:{uyruk}, ANNE ADI:{nufus_il}, "
                f"DOĞUM TARİHİ:{dogum_tarihi}, NUFUS İL:{ana_adi}, NUFUS İLÇE:{baba_adi}, ANNE TC:{nufus_ilce}\n".encode())    

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
