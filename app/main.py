from fastapi import FastAPI

from app.core.database import init_db
from app.routers.home import router as home_router
from app.routers.auth import router as auth_router


app = FastAPI(
    title="Note Taking API",
    description="Backend API for a Note Taking application",
    version="1.0.0"
)

app.include_router(home_router) 
app.include_router(auth_router)
init_db(app)