from fastapi import APIRouter, status, UploadFile, File
from .service import s2t_sevice

router = APIRouter()  # init router

# hello world
@router.get("/", status_code=status.HTTP_200_OK)
def index():
    return {"message": "hello"}

# 
@router.post("/s2t", status_code=status.HTTP_201_CREATED)
def s2t_prediction(file: UploadFile = File(...)):
    file_data = file.filename
    return {"message": file_data}
