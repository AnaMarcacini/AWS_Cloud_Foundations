import os
import markdown
import pdfkit

# Caminho da pasta onde o script está localizado
pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_md = pasta_atual

# Arquivo de saída único
pdf_unico = os.path.join(pasta_atual, "Notas_Completas.pdf")

# Ordena os arquivos "Module x Notes.md" de 1 a 10
arquivos_md = sorted([f for f in os.listdir(pasta_md) if f.startswith("Module") and f.endswith("Notes.md")],
                     key=lambda x: int(x.split()[1]))

# Concatenar conteúdo dos arquivos em uma única string HTML
conteudo_completo_html = ""
for arquivo in arquivos_md:
    caminho_md = os.path.join(pasta_md, arquivo)

    with open(caminho_md, "r", encoding="utf-8") as f:
        conteudo_md = f.read()
        
    conteudo_html = markdown.markdown(conteudo_md)
    conteudo_completo_html += conteudo_html + "<hr>"

# Converte o HTML combinado para um único PDF
pdfkit.from_string(conteudo_completo_html, pdf_unico)

print(f"PDF único {pdf_unico} criado com sucesso!")
