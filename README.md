# Era Product API

## Tech Used
<b>Built with</b>
- [Flask](https://github.com/pallets/flask)
- [Docker](https://www.docker.com)
- [Postgresql](https://www.postgresql.org)

---
## Getting Started


### Prerequisites

```
docker
docker-compose
girlfriend (optional)
```

### Installing

```bash
$ git clone
$ bash start.sh
```
---
## Development

### Start Development
```bash
# create virtual environment
$ virtualenv .venv
$ source .venv/bin/activate

# install dependency
$ pip install -r requirements.txt

#export env variable from .env file
$ export $(cat .env | xargs) && rails c 
$ make run 
```

### Running the Tests
```bash
#export env variable from .env file
$ export $(cat .env | xargs) && rails c
$ make test
```

### Migrate & Upgrade Database
```bash
#export env variable from .env file
$ export $(cat .env | xargs) && rails c
$ make migrate
$ make upgrade
```
---
## Architecture

![Alt text](/architecture.png?raw=true "architecture")

Project ini saya asumsikan sebagai aplikasi monolitic. Arsitektur yang digunakan adalah Layer yang dikelompokan per domain. 
1. Services : Berisi logika aplikasi
2. Models : Berfungsi sebagai representatif dari data/database
3. Routes : Berfungsi untuk mengatur lalu lintas file berdasarkan request

Untuk aplikasi monolitik, desain seperti akan sangat membantu di masa depan jika sudah banyak fitur dan banyak juga engineer yang mengerjakan. Perubahan code didalam fitur product sangat kecil kemungkinan menyebabkan perubahan di fitur 1 atau fitur 2, memperkecil kemungkinan git conflict. 

---
## API

#### show product terbaru
GET http://localhost:5000/v1/product?by=created_at&order=desc

#### show product harga termurah
GET http://localhost:5000/v1/product?by=price&order=asc

#### show product harga termahal
GET http://localhost:5000/v1/product?by=price&order=desc

#### show product name (A-Z)
GET http://localhost:5000/v1/product?by=name&order=asc

#### show product name (Z-A)
GET http://localhost:5000/v1/product?by=name&order=desc

#### pagination
GET http://localhost:5000/v1/product?by=name&order=asc&page=1&limit=10

#### add Product
POST http://localhost:5000/v1/product
```json
    {
        "name" : "Apple MacBook Air M2 (2022)",
        "description" : "Bertenaga super berkat chip M2....",
        "quantity" : 10,
        "price" : 19999000
    }
```