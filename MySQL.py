import mysql.connector
import pyfirmata
import datetime

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="elev",
database="iot"
)

mycursor = mydb.cursor()

print("Connected..") # skriver når den starter

sql = "INSERT INTO sensor2(verdi,tid) VALUES (%s,%s)"

verdi = 1.0 # Verdi som blir skrevet til databasen(sensor-verdi(float))
tid = datetime.datetime.now() #Tid som blir skrevet til databasen(sensor - tid(datetime))

id=1

board = pyfirmata.Arduino('COM4') #arduino porten

it = pyfirmata.util.Iterator(board)
it.start()
analog_input = board.get_pin('a:1:i') # pinnen til potentiometer.

potval = analog_input.read() #gjer at det blir forandring

val = (verdi, tid)

print("Executing...") #skriver når den holder på

mycursor.execute(sql, val)
mydb.commit()

print("Done") # skriver det når den er ferdig

