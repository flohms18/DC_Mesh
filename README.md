# Small Data Mesh Example

This is a hands-on example of a small Data Mesh implemented in Python. The project demonstrates the core principles of a Data Mesh: **decentralized ownership**, **self-service access**, and **discoverable data products**.  

In this example, the data products are based on **DC superheroes**, each containing information about the character’s secret identity and ownership.

---

## Project Structure

project/
│
├─ domains/
│ ├─ batman.py
│ └─ superman.py
│
├─ registry.py
└─ main.py

- **domains/** – Contains the data products (`batman.py` and `superman.py`).  
- **registry.py** – Keeps track of all existing data products and their URLs.  
- **main.py** – Entry point for requesting and interacting with the data products.  

## Requirements

- Python 3.10 or higher  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)

---

## Setup

1. **Clone the repository**  
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Create a virtual environment (to avoid dependency conflicts)**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the app**
    ```bash
    uvicorn main:app --reload
    uvicorn domains.batman:app --reload --port 8001
    uvicorn domains.superman:app --reload --port 8002
    ```
5.**Access the web interface**
    http://127.0.0.1:8000/docs


## Add new products

1. Create a new file within the domains folder
```python
from fastapi import FastAPI

app = FastAPI(title=" -------- Domain")

Batman_Data = [
    {"firstname" : 'Bruce', 'lastname' : 'Wayne'} #Replace Data with your own 
]

@app.get("/-----") #update the URL
def get_batman_data():
    return {
        "data" : Batman_Data, # update the data
        "owner" : "Wayne Enterprises" # update the data
    }
```
2. **Update registry.py**
    ```python
    DATA_Products = {
    "batman" : "http://127.0.0.1:8001/batman",
    "superman" : "http://127.0.0.1:8002/superman",
    "new_product" : "http://127.0.0.1:8003/new_product" #update the name and URL of your new data product
    }
```
```

5. **Access the web interface**
    http://127.0.0.1:8000/docs
```



