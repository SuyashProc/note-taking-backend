from fastapi import APIRouter

router = APIRouter(
    tags=["Home"],
)

@router.get("/")
def read_root():
    return {"message": "Hello World"}