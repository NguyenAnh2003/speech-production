import uvicorn
from myapp.app import init_app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_delay=0.5,
        use_colors=True,
    )
