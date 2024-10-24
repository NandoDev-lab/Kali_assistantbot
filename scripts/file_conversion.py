import PyPDF2 # type: ignore

def convert_file(file_path):
    """
    Converte um arquivo PDF em texto.

    Args:
        file_path (str): Caminho para o arquivo PDF a ser convertido.
    """
    # Abre o arquivo PDF
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""

        # Extrai o texto de cada página do PDF
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
        
        # Salva o texto extraído em um arquivo .txt
        with open('converted_file.txt', 'w') as text_file:
            text_file.write(text)
    
    print("Conversão concluída!")
