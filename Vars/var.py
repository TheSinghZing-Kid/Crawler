url = ["https://craz.ca/monitoring/calgary-central/", "https://craz.ca/monitoring/calgary-southeast/", "https://craz.ca/monitoring/calgary-northwest/"]
sql = """INSERT INTO yyc_central (datetime, NO, NO2, NOX, CH4, PM25, THC, CO, O3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
sql_se = """INSERT INTO yyc_se (datetime, NO, NO2, NOX, CH4, PM25, THC, CO, O3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
sql_nw = """INSERT INTO yyc_nw (datetime, NO, NO2, NOX, CH4, PM25, THC, CO, O3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""