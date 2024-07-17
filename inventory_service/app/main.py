from fastapi import FastAPI
import asyncio 
from app.db.db_connector import create_db_and_tables
from app.routes.inventory_routes import router

 

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to Inventory service"

app.include_router(router=router)