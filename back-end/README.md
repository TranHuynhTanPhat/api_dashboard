# api-dashboard-BackEnd

### Pre: [Python3](https://www.python.org/)


## Project setup


### Create virtual environment
```
python3 -m venv venv
```

### Run virtual environment
```
source venv/bin/activate
```

### Install libraries (in zsh terminal)
```
pip install fastapi uvicorn pymongo
```

### Run server with uvicorn
```
uvicorn index:app --reload
```

### If URL of Server is different from http://127.0.0.1:8000
### Change it from FrontEnd
