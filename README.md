# 📄 Relatório de Investimentos em PDF com Upload para AWS S3

Este projeto consiste em um script Python que **gera um relatório de
investimentos em PDF** utilizando a biblioteca **ReportLab** e,
opcionalmente, realiza o **upload do arquivo para um bucket da AWS S3**
usando o **Boto3**.

## 🚀 Funcionalidades

-   Criação de um PDF chamado **`relatorio_investimentos.pdf`**
-   Inserção de:
    -   Título do relatório
    -   Lista de investimentos (investidor, tipo, valor e data)
-   Estrutura pronta para upload do arquivo para a **AWS S3**
-   Código simples e didático

## 🛠 Tecnologias Utilizadas

-   Python 3
-   ReportLab
-   Boto3 (AWS SDK)

## 📦 Dependências

``` bash
pip install reportlab boto3
```

## ▶️ Como Executar

``` bash
python main.py
```

## ☁️ AWS S3 (Opcional)

Para enviar o PDF ao S3: 1. Configure suas credenciais com
`aws configure` 2. Descomente a linha:

``` python
s3.upload_file(pdf_file_path, bucket_name, object_name)
```

## 📌 Observações

-   O upload está desativado por padrão
-   Ideal para estudos acadêmicos e demonstrações

## 📚 Possíveis Melhorias

-   Ler dados de CSV ou banco de dados
-   Criar tabelas no PDF
-   Automatizar geração em múltiplas páginas
