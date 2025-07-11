from pydantic import BaseModel

class QuestionPreview(BaseModel):
    numero: str
    enunciado: str

    @staticmethod
    def from_csv_row(row):
        return QuestionPreview(numero=row[0], enunciado=row[1])
