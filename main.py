from fastapi import FastAPI
import os
from todos_api.models import Base
from todos_api.database import engine
from todos_api.routers import auth, todos, admin, users
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(
     title="Task Tracker API",
    description="""
    A RESTful API for tracking tasks.
    
    ## Features
    
    * User authentication and authorization
    * Task creation, updates, and deletion
    * Administrative controls
    * User management
    
    ## Authentication
    
    Most endpoints require authentication via JWT token.
    """,
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# health check
@app.get("/healthy")
def health_check():
    return {'status', 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 10000))
    
    uvicorn.run(app, host="0.0.0.0", port=port)
