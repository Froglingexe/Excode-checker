import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="secmen"
)


if db.is_connected():
    print("Veritabanına başarıyla bağlandı. NOT: Adresi bulması 2-3 dakika arası değişebilir.")

tc = input("Lütfen TC kimlik numarasını girin: ")


cursor = db.cursor()
cursor.execute(f"SELECT * FROM secmen2015 WHERE TC = '{tc}'")
result = cursor.fetchone()


with open("sonuc.txt", "a", encoding="utf-8") as f:
    if result:
        adresil = result[11]
        adresilce = result[12]
        mahalle = result[13]
        cadde = result[14]
        daireno = result[15]
        kapino = result[16]
        engel = result[17]
        f.write(f"Kendi: TC : {tc} ADRES İL : {adresil}  ADRES İLÇE : {adresilce} MAHALLE: {mahalle} CADDE {cadde} DAİRE NO: {daireno} KAPI NO: {kapino} ENGELİ: {engel}\n")
        print(f"Kendi: TC : {tc} ADRES İL : {adresil}  ADRES İLÇE : {adresilce} MAHALLE: {mahalle} CADDE {cadde} DAİRE NO: {daireno} KAPI NO: {kapino} ENGELİ: {engel}")
    else:
        f.write(f"{tc} için sonuç bulunamadı.\n")
        print(f"{tc} için sonuç bulunamadı.")

# Bağlantıyı kapat
db.close()
