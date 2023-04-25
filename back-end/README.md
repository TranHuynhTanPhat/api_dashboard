# api-dashboard-BackEnd

### Pre: [Python3](https://www.python.org/)

## Project setup

### Create virtual environment

```
python3 -m venv venv
```

### Run virtual environment

#### Macos

```
source venv/bin/activate
```

#### Windows

```
venv/Scripts/activate
```

### Install libraries (in zsh terminal)

```
pip3 install -r requirements.txt
```

### Run server with uvicorn

```
uvicorn app.index:app --reload
```

### If URL of Server is different from http://127.0.0.1:8000

### Change it from FrontEnd

## Docker

### Run Docker desktop

```
docker-compose up -d
```
