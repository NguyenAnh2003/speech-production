from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route import router

def init_app() -> FastAPI:
    # init fast api app
    try:
        # init FastAPI object
        app = FastAPI()

        # middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # router
        app.include_router(router=router)

    except Exception as e:
        raise ValueError(e.__cause__)
