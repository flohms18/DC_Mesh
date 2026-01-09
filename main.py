from fastapi import FastAPI,HTTPException
import httpx
from registry import list_data_products, get_product_url

app = FastAPI(title="DC_Mesh")

@app.get("/products")
def products():
    return {
        "products" : list_data_products()
    }

@app.get("/products/{product_name}")
def fetch_product(product_name: str):
    url = get_product_url(product_name)
    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except httpx.RequestError as e:
        # Network / DNS / connection errors
        raise HTTPException(
            status_code=502,
            detail=f"Cannot reach data product: {e}"
        )

    except httpx.HTTPStatusError as e:
        # Data product returned 4xx or 5xx
        raise HTTPException(
            status_code=502,
            detail=f"Data product error: {e.response.text}"
        )