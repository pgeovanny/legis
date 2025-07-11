import pdfplumber
import docx
import csv
import io
from app.schemas.question import QuestionPreview

async def extract_questions_from_file(file, banca, quantidade) -> list:
    filename = file.filename.lower()
    questions = []
    content = await file.read()
    if filename.endswith('.pdf'):
        text = ""
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        questions = smart_extract_questions(text, banca, quantidade)
    elif filename.endswith('.docx'):
        doc = docx.Document(io.BytesIO(content))
        text = "\n".join([p.text for p in doc.paragraphs])
        questions = smart_extract_questions(text, banca, quantidade)
    elif filename.endswith('.csv'):
        reader = csv.reader(io.StringIO(content.decode('utf-8')))
        rows = list(reader)
        questions = [QuestionPreview.from_csv_row(row) for row in rows[:quantidade]]
    elif filename.endswith('.txt'):
        text = content.decode('utf-8')
        questions = smart_extract_questions(text, banca, quantidade)
    return questions

def smart_extract_questions(text: str, banca: str, quantidade: int) -> list:
    import re
    q_pattern = re.compile(r'(\d+)[)\.]\s*(.+?)(?=\n\d+[)\.]|\Z)', re.DOTALL)
    matches = list(q_pattern.finditer(text))
    extracted = []
    for match in matches[:quantidade]:
        question = match.group(2).strip()
        extracted.append(QuestionPreview(numero=match.group(1), enunciado=question))
    return extracted
