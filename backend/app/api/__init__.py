from fastapi import APIRouter
from app.api.upload import router as upload_router
from app.api.export import router as export_router
from app.api.auth import router as auth_router
router = APIRouter()
router.include_router(upload_router, prefix='/upload', tags=['Upload'])
router.include_router(export_router, prefix='/export', tags=['Export'])
router.include_router(auth_router, prefix='/auth', tags=['Auth'])
