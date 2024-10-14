import machine
import dht
import mysql.connector

# Konfigurasi koneksi MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
  database="db_baru"
)

mycursor = mydb.cursor()

# Inisialisasi sensor DHT11
d = dht.DHT11(pin=18)  

while True:
    try:
        d.measure()
        temp = d.temperature
        humi = d.humidity

        # Simpan data ke MySQL
        sql = "INSERT INTO readings (temperature, humidity) VALUES (%s, %s)"
        val = (temp, humi)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Data berhasil disimpan ke MySQL!")
    except RuntimeError as error:
        print(error.args[0])

    time.sleep(2)

mydb.close()
