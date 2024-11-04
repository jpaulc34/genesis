from fastapi import FastAPI

from app.api.categories import category_router
from app.api.products import product_router
from app.api.inventories import inventory_router
from app.api.users import user_router
from app.core.database import lifespan

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(user_router.router)
    app.include_router(category_router.router)
    app.include_router(product_router.router)
    app.include_router(inventory_router.router)
    return app

app = create_app()
