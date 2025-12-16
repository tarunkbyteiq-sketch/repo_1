from fastapi import FastAPI
from routes import router

app = FastAPI(title="Two-Fil FastAPI App")

# include routes from routes.py
app.include_router(router)
