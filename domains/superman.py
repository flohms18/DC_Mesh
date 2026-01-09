from fastapi import FastAPI

app = FastAPI(title="Superman Domain")

Superman_Data = [
    {"firstname" : 'Clark', 'lastname' : 'Kent'}
]

@app.get("/superman")
def get_batman_data():
    return {
        "data" : Superman_Data,
        "owner" : "Daily Planet"
}