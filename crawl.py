import selenium.webdriver as Wd
from selenium.webdriver.chrome.options import Options
from Vars.conn import *
from Vars.var import *
import mysql.connector as MC
import bs4 as B



cursor = conn.cursor()
print("created cursor to database: " + db)


def ce():
    print("getting data from: " + url[0])
    url_ce = url[0]
    ce_driver = Wd.Chrome() 
    print("Opening page: " + url_ce)
    ce_driver.get(url_ce)
    print("Find the Button")
    button = ce_driver.find_element_by_xpath("""//*[@id="mainTable"]/span/a""")
    button.click()
    print("Clicked Button")
    loop = 1 
    td = 1
    tr_num = 5
    row = []
    #there are 124 rows on the table i am scraping from. if there are more than 124 rows, add 1 to total amount of rows.
    while loop < 125:
        print("runnig main loop iteration #: " + str(loop))
        #this while loop has to run ten times, as there are 9 elements columns to scrape from.
        #If there are more than modify as needed.
        while td < 10: 
            print("running secondary loop iteration #: " + str(td))
            xpath = '//*[@id="tableDisplay"]/table/tbody/tr[' + str(tr_num) + ']/td[' + str(td) + ']'
            tr = ce_driver.find_element_by_xpath(xpath)
            tr_html = tr.get_attribute("outerHTML") 
            soup = B.BeautifulSoup(tr_html, 'html.parser')
            text = soup.get_text()
            row.append(text)
            
            td += 1
        
        
        if row[1] == 'NaN' and row[2] == 'NaN' and row[3] == 'NaN' and row[4] == 'NaN' and row[5] == 'NaN' and row[6] == 'NaN' and row[7] == 'NaN' and row[8] == 'NaN':
            loop = 125
            
            ce_driver.close()

        else:
        
            for n, i in enumerate(row):
                if i == 'NaN':
                    row[n] = '0.0'   

        
            cursor.execute(sql, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            conn.commit()
            td = 1
            row.clear()
            tr_num += 1
            loop += 1
    
        

    
    
def se(): 
    print("getting data from: " + url[1])
    url_se = url[1]
    se_driver = Wd.Chrome() 
    print("Opening page: " + url_se)
    se_driver.get(url_se)
    print("Find the Button")
    button = se_driver.find_element_by_xpath("""//*[@id="mainTable"]/span/a""")
    button.click()
    print("Clicked Button")
    loop = 1 
    td = 1
    tr_num = 5
    row = []
    #there are 124 rows on the table i am scraping from. if there are more than 124 rows, add 1 to total amount of rows.
    while loop < 125:
        print("runnig main loop iteration #: " + str(loop))
        #this while loop has to run ten times, as there are 9 elements columns to scrape from.
        #If there are more than modify as needed.
        while td < 10: 
            print("running secondary loop iteration #: " + str(td))
            xpath = '//*[@id="tableDisplay"]/table/tbody/tr[' + str(tr_num) + ']/td[' + str(td) + ']'
            tr = se_driver.find_element_by_xpath(xpath)
            tr_html = tr.get_attribute("outerHTML") 
            soup = B.BeautifulSoup(tr_html, 'html.parser')
            text = soup.get_text()
            row.append(text)
            
            td += 1
        
        
        if row[1] == 'NaN' and row[2] == 'NaN' and row[3] == 'NaN' and row[4] == 'NaN' and row[5] == 'NaN' and row[6] == 'NaN' and row[7] == 'NaN' and row[8] == 'NaN':
            loop = 125
           
            se_driver.close()

        else:
        
            for n, i in enumerate(row):
                if i == 'NaN':
                    row[n] = '0.0'   

        
            cursor.execute(sql_se, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            conn.commit()
            td = 1
            row.clear()
            tr_num += 1
            loop += 1    
    




def nw():
    print("getting data from: " + url[2])
    url_nw = url[2]
    nw_driver = Wd.Chrome() 
    print("Opening page: " + url_nw)
    nw_driver.get(url_nw)
    print("Find the Button")
    button = nw_driver.find_element_by_xpath("""//*[@id="mainTable"]/span/a""")
    button.click()
    print("Clicked Button")
    loop = 1 
    td = 1
    tr_num = 5
    row = []
    #there are 124 rows on the table i am scraping from. if there are more than 124 rows, add 1 to total amount of rows.
    while loop < 125:
        print("runnig main loop iteration #: " + str(loop))
        #this while loop has to run ten times, as there are 9 elements columns to scrape from.
        #If there are more than modify as needed.
        while td < 10: 
            print("running secondary loop iteration #: " + str(td))
            xpath = '//*[@id="tableDisplay"]/table/tbody/tr[' + str(tr_num) + ']/td[' + str(td) + ']'
            tr = nw_driver.find_element_by_xpath(xpath)
            tr_html = tr.get_attribute("outerHTML") 
            soup = B.BeautifulSoup(tr_html, 'html.parser')
            text = soup.get_text()
            row.append(text)
            
            td += 1
        
        
        if row[1] == 'NaN' and row[2] == 'NaN' and row[3] == 'NaN' and row[4] == 'NaN' and row[5] == 'NaN' and row[6] == 'NaN' and row[7] == 'NaN' and row[8] == 'NaN':
            loop = 125
            conn.close()
            nw_driver.close()

        else:
        
            for n, i in enumerate(row):
                if i == 'NaN':
                    row[n] = '0.0'   

        
            cursor.execute(sql_nw, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            conn.commit()
            td = 1
            row.clear()
            tr_num += 1
            loop += 1

ce()
se()
nw()