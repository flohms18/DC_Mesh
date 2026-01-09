from fastapi import FastAPI

app = FastAPI(title="Batman Domain")

Batman_Data = [
    {"firstname" : 'Bruce', 'lastname' : 'Wayne'}
]

@app.get("/batman")
def get_batman_data():
    return {
        "data" : Batman_Data,
        "owner" : "Wayne Enterprises"
    }