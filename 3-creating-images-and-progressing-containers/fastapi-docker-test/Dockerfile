#Imagem base do python
FROM python:3.11-slim

#Diretório de trabalho dentro do container
WORKDIR /app

#Copiando o arquivo de requisitos para o container
COPY requirements.txt .

#Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

#Copiando o restante dos arquivos do projeto para o container
COPY . .

#Expondo a porta que o FastAPI irá rodar
EXPOSE 8000

#Comando para rodar a aplicação
CMD [ "python", "main.py" ]