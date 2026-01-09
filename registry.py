DATA_Products = {
    "batman" : "http://127.0.0.1:8001/batman",
    "superman" : "http://127.0.0.1:8002/superman"

}

def list_data_products():
    return list(DATA_Products.keys())

def get_product_url(name : str):
    return DATA_Products.get(name)