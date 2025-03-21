# Usando a imagem oficial do Python como base
FROM python:3.10-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de requisitos para o container
COPY requirements.txt .

# Instalando as dependências do Django
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código do projeto para dentro do container
COPY . .

# Expondo a porta do Django
EXPOSE 8000

# Comando para rodar o servidor Django no modo de produção com Gunicorn
CMD ["gunicorn", "fabio.wsgi:application", "--bind", "0.0.0.0:8000"]