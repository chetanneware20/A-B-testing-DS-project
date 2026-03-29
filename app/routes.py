
from fastapi import APIRouter
from app.ab_test import run_ab_test

router = APIRouter()

@router.get("/ab-test")
def ab_test():
    result = run_ab_test()
    return result
