from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import boto3

def create_investment_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Relatório de Investimentos")
    
    c.setFont("Helvetica", 12)
    investments = [
        {"Investidor": "João Silva", "Tipo": "Ações", "Valor": "R$ 10.000,00", "Data": "01/01/2024"},
        {"Investidor": "Maria Oliveira", "Tipo": "Fundos Imobiliários", "Valor": "R$ 5.000,00", "Data": "15/02/2024"},
        {"Investidor": "Carlos Souza", "Tipo": "Tesouro Direto", "Valor": "R$ 8.000,00", "Data": "20/03/2024"}
    ]
    
    y = 720
    for investment in investments:
        c.drawString(100, y, f"Investidor: {investment['Investidor']}")
        c.drawString(100, y-15, f"Tipo: {investment['Tipo']}")
        c.drawString(100, y-30, f"Valor: {investment['Valor']}")
        c.drawString(100, y-45, f"Data: {investment['Data']}")
        y -= 75
    
    c.save()

pdf_file_path = "relatorio_investimentos.pdf"

create_investment_pdf(pdf_file_path)

s3 = boto3.client('s3')
bucket_name = 'aulafiap1'
object_name = pdf_file_path

#s3.upload_file(pdf_file_path, bucket_name, object_name)

print(f"PDF '{pdf_file_path}' criado e enviado para o bucket S3 '{bucket_name}/{object_name}'.")  