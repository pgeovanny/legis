from fastapi import APIRouter, Response
from typing import List
from app.schemas.question import QuestionPreview
from app.services.docx_exporter import generate_docx_summary

router = APIRouter()

@router.post("/docx")
async def export_docx(questions: List[QuestionPreview], resumo: str, logo_path: str = None):
    docx_bytes = generate_docx_summary(questions, resumo, logo_path)
    return Response(docx_bytes, headers={
        'Content-Disposition': 'attachment; filename="resumo.docx"'
    }, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
