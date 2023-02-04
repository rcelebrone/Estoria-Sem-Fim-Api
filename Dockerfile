# Use uma imagem base do Python
FROM python:3.9-slim-buster

# Configure o diretório de trabalho
WORKDIR /app

# Instale as dependências do Flask
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie o arquivo da sua aplicação para o diretório de trabalho
COPY app.py .

# Defina a porta para ouvir solicitações
EXPOSE 5000

# Defina o comando de inicialização
CMD ["python", "app.py"]
