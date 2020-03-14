#imports
import mysql.connector as MC
#variables
host = "192.168.1.90"
pwd = "123Lion!@#"
usrname = "Veer"
db = "pollution"
auplug = "mysql_native_password"
#connection
conn = MC.connect(
    host=host,
    passwd=pwd,
    user=usrname,
    database=db,
    auth_plugin=auplug
)