from fastapi import FastAPI
from app.repositories.product_repository import ProductRepository
from app.repositories.order_repository import OrderRepository
from app.services.product_service import ProductService
from app.api.product_api import router, init_product_api

app = FastAPI()   # THIS MUST EXIST

# Load data
product_repo = ProductRepository("app/data/products.json")
order_repo = OrderRepository("app/data/orders.json")

product_service = ProductService(product_repo, order_repo)
init_product_api(product_service)

app.include_router(router, prefix="/api")
