import os
import markdown
import pdfkit #pip install markdown pdfkit #sudo apt-get install wkhtmltopdf

# Caminho da pasta com arquivos .md
pasta_md = os.path.dirname(os.path.abspath(__file__))

pasta_pdf =  os.path.join(pasta_md, "pdfs")

# Cria a pasta de saída se não existir
os.makedirs(pasta_pdf, exist_ok=True)

for arquivo in os.listdir(pasta_md):
    if arquivo.endswith(".md"):
        caminho_md = os.path.join(pasta_md, arquivo)

        # Lê o conteúdo do arquivo .md
        with open(caminho_md, "r", encoding="utf-8") as f:
            conteudo_md = f.read()

        # Converte markdown para HTML
        conteudo_html = markdown.markdown(conteudo_md)

        # Define o caminho de saída do PDF
        nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
        caminho_pdf = os.path.join(pasta_pdf, nome_pdf)

        # Converte HTML para PDF
        pdfkit.from_string(conteudo_html, caminho_pdf)

        print(f"{nome_pdf} criado com sucesso!")


