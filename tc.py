import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="101m"
)


if db.is_connected():
    print("Veritabanına başarıyla bağlandı.")

tc = input("Lütfen TC kimlik numarasını girin: ")


cursor = db.cursor()
cursor.execute(f"SELECT * FROM 101m WHERE TC = '{tc}'")
result = cursor.fetchone()


with open("tcsorgu.txt", "a", encoding="utf-8") as f:
    if result:
        adi = result[2]
        soyadi = result[3]
        dogum_tarihi = result[4]
        nufus_yeri = result[5]
        ilce = result[6]
        anne_adi = result[7]
        anne_tc = result[8]
        baba_adi = result[9]
        baba_tc = result[10]
        uyruk = result[11]
        f.write(f"Kendi: TC : {tc} ADI : {adi}  SOYADI : {soyadi} DOĞUM TARİHİ: {dogum_tarihi} NÜFUS İL: {nufus_yeri} NÜFÜS İLÇE: {ilce} ANNE ADI: {anne_adi} ANNE TC: {anne_tc} BABA ADI: {baba_adi} BABA TC: {baba_tc} UYRUK: {uyruk}\n")
        print(f"Kendi: TC : {tc} ADI : {adi}  SOYADI : {soyadi} DOĞUM TARİHİ: {dogum_tarihi} NÜFUS İL: {nufus_yeri} NÜFÜS İLÇE: {ilce} ANNE ADI: {anne_adi} ANNE TC: {anne_tc} BABA ADI: {baba_adi} BABA TC: {baba_tc} UYRUK: {uyruk}")
    else:
        f.write(f"{tc} için sonuç bulunamadı.\n")
        print(f"{tc} için sonuç bulunamadı.")

# Bağlantıyı kapat
db.close()
