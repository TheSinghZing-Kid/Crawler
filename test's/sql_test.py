import mysql.connector as MC
#sucsseful

host = "192.168.1.90"
pwd = "123Lion!@#"
usrname = "Veer"
db = "pollution"
auplug = "mysql_native_password"

conn = MC.connect(
    host=host,
    passwd=pwd,
    user=usrname,
    database=db,
    auth_plugin=auplug
)

row = ['2020/02/19 05:00', '85.663', '40.484', '126.147', '2.625', '0.589', '0.706', '11.595', '2.625']
row2 = ['2020/02/19 06:00', '85.663', '40.484', 'NaN', '2.625', 'NaN', '0.706', '11.595', '2.625']
row3 = ['2020/02/19 07:00', '85.663', 'NaN', '126.147', '2.625', '0.589', 'NaN', '11.595', '2.625']

for n, i in enumerate(row2):
     if i == 'NaN':
        row2[n] = '0.0'

for a, b in enumerate(row3):
     if b == 'NaN':
        row3[a] = '0.0'

cursor = conn.cursor()
sql = """INSERT INTO yyc_nw (datetime, NO, NO2, NOX, CH4, PM25, THC, CO, O3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
print(row2)
print(row3)

cursor.execute(sql, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
cursor.execute(sql, (row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7], row2[8]))
cursor.execute(sql, (row3[0], row3[1], row3[2], row3[3], row3[4], row3[5], row3[6], row3[7], row3[8]))

conn.commit()
conn.close()