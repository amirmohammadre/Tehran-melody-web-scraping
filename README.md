# Tehran Melody Web Scraper: Track Special Sale Products Efficiently

A Python-based web scraper for tracking special sale products on the Tehran Melody website.
This program automatically retrieves the list of discounted products from the Tehran Melody website and processes the data for efficient storage and analysis.

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


