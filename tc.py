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
tc = input("Sorgulanacak kişinin TC'sini giriniz: ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = tc + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    if tc:
        sql = f"SELECT * FROM 101m WHERE TC = '{tc}'"
    else:
        sql = f"SELECT * FROM 101m WHERE TC = '{tc}'"



    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "wb") as dosya:
        for kayit in mycursor:
            tc = kayit[1]
            adi = kayit[2]
            soyadi = kayit[3]
            dogum_tarihi = kayit[4] 
            nufus_il = kayit[5]
            nufus_ilce = kayit[6]
            ana_adi = kayit[7]           
            ana_tc = kayit[8]           
            baba_adi = kayit[9]
            baba_tc = kayit[10]
            uyruk = kayit[11]

            
            dosya.write(f"TC:{tc}, ADI:{adi}, SOYADI:{soyadi}, DOĞUM TARIHI:{dogum_tarihi}, NUFUS İL:{nufus_il}, NUFUS İLÇE:{nufus_ilce}"
                        f"ANNE ADI:{ana_adi}, ANNE TC:{ana_tc}, BABA ADI:{baba_adi}, BABA TC:{baba_tc}, UYRUK:{uyruk}\n".encode())
            

            print(f"TC:{tc}, ADI:{adi}, SOYADI:{soyadi}, DOĞUM TARIHI:{dogum_tarihi}, NUFUS İL:{nufus_il}, NUFUS İLÇE:{nufus_ilce}"
                        f"ANNE ADI:{ana_adi}, ANNE TC:{ana_tc}, BABA ADI:{baba_adi}, BABA TC:{baba_tc}, UYRUK:{uyruk}\n".encode())  

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
