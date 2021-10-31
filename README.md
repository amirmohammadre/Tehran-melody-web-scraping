# Tehran Melody Web Scraping 

This program Receives the list of products for special sale on the Tehran Melody website and places them one the Redis database. Also, a list of products equal to or above the 10% discount is created in the sales.txt file.

---

### **How to run**:

```
python3 main.py

redis-cli --raw

HGETALL Products
```

### **How to run with Docker**:

```
sudo docker build -t myapp:v1 .

sudo docker network create mynet

sudo docker run -d --net mynet --name redis-server redis:latest

sudo docker run --rm -it --name pyapp --net mynet -e REDIS_HOST=redis-server myapp:v1
```

### **How to run with Docker Compose**:

```
sudo docker-compose up
```


