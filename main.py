"""import libraries"""
import requests
import re
import redis
import time as tm
from bs4 import BeautifulSoup


"""information about redis"""
redis_host = 'localhost'
redis_port = 6379
redis_db   = 0
redis_pass = ""

try:
    """Connect to database redis"""
    conn = redis.Redis(host=redis_host, port=redis_port, db=redis_db,
    password=redis_pass, decode_responses=True)

except Exception as rsn:
    print("[-] I can not connect to redis database !!", str(rsn))
    exit()
