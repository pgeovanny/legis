from app.services.extractor import smart_extract_questions

def test_extractor_basico():
    texto = "1) O que é Python?\n2) O que é uma API?"
    resultado = smart_extract_questions(texto, 'FCC', 2)
    assert len(resultado) == 2
    assert resultado[0].enunciado == "O que é Python?"
