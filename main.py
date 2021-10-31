
"""import libraries"""
import requests
import re
import redis
import time as tm
import os
from bs4 import BeautifulSoup


"""information about redis"""
redis_host = 'localhost'
redis_port = 6379
redis_db   = 0
redis_pass = ""


"""This function is related to web scraping"""
def Scraper():
    res    = requests.get('https://www.tehranmelody.com/special-offers?limit=100')
    soup   = BeautifulSoup(res.text, 'html.parser')

    products_name  = soup.find_all('h3', attrs={'class':'dir-ltr mt-4'}) 
    products_price = soup.find_all('div', attrs={'class':'price'})

    for p_name, p_price in zip(products_name, products_price):
        conn.hset("Products", re.sub(r'\s+',' ', p_name.text).strip(), re.sub(r'\s+',' ', p_price.text).strip())

    
    """List of products above 10% discount with name and price"""
    products_sale = soup.find_all('span', attrs={'class':'sale-percent en-font small'})

    fout = open("sales.txt", "w") 

    for p_sale, p_name, p_price in zip(products_sale, products_name, products_price):
        if int(float(re.sub(r'\%+', '',p_sale.text))) >= 10:
            fout.write(p_sale.text.strip() + " " + p_name.text.strip() + " = " + p_price.text.strip() + "\n")
            
    fout.close()


try:
    """Connect to database redis"""
    conn = redis.Redis(host=os.environ.get("REDIS_HOST", redis_host)
    , port=int(os.environ.get("REDIS_PORT", redis_port)), db=redis_db, 
    password=redis_pass, decode_responses=True)

except Exception as rsn:
    print("[-] I can not connect to redis database !!", str(rsn))
    exit()

else:
    """Insert time"""
    time_ = tm.time()
    current_time = tm.ctime(time_)
    mesg = "Success Connection To Redis Database {}"
    print(mesg.center(100, "*").format(current_time))
    tm.sleep(1)

    """Extracting information from Tehran Melody website"""
    print("Tehran Melody Special Sale Products".center(100,"*"))
    Scraper()
    numbers = conn.hlen("Products")
    print("""\n%s Products were successfully added to the database ;)
    \nPlease check the database to display products and their prices""" % (numbers))

    print("Also, a list of products equal to or above the 10% discount is created in the sales.txt file")

