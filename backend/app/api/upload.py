from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Depends
from typing import List
from app.services.extractor import extract_questions_from_file
from app.schemas.question import QuestionPreview
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/questions", response_model=List[QuestionPreview])
async def upload_questions(
    file: UploadFile = File(...),
    banca: str = Form(...),
    quantidade: int = Form(...),
    user=Depends(get_current_user)
):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
        "text/csv"]:
        raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado")
    questions = await extract_questions_from_file(file, banca, quantidade)
    if not questions:
        raise HTTPException(status_code=422, detail="Não foi possível extrair questões")
    return questions
