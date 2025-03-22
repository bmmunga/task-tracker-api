from fastapi import FastAPI
from todos_api.models import Base
from todos_api.database import engine
from todos_api.routers import auth, todos, admin, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

# health check
@app.get("/healthy")
def health_check():
    return {'status', 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
