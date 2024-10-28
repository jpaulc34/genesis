from fastapi import FastAPI
from app.routers import user_router, category_router, product_router

from app.core.database import lifespan

app = FastAPI(lifespan=lifespan)

# Include the User Router
app.include_router(user_router.router)
app.include_router(category_router.router)
app.include_router(product_router.router)