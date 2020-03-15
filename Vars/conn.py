#imports
import mysql.connector as MC
#variables
host = "ip to MySQL server"
pwd = "pwd to MySQL server"
usrname = "MySQL username"
db = "Database"
auplug = "mysql_native_password"
#connection
conn = MC.connect(
    host=host,
    passwd=pwd,
    user=usrname,
    database=db,
    auth_plugin=auplug
)
