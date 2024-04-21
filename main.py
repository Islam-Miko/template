import uvicorn
from app.server import app

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        reload=False,
        workers=1,
    )

