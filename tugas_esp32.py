import machine
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="tugas_led"  
)

mycursor = mydb.cursor()

while True:
    try:
        led_pin = machine.Pin(2, machine.Pin.OUT)  
        kondisi = 1 if led_pin.value() == 1 else 0  

        sql = "INSERT INTO dataled (kondisi) VALUES (%s)"
        val = (temp, humi, kondisi)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Data berhasil disimpan ke MySQL!")
    except RuntimeError as error:
        print(error.args[0])

    time.sleep(2)

mydb.close()
