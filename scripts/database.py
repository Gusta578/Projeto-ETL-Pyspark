from sqlalchemy.orm import declarative_base
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

Base = declarative_base()

# Preparando a leitura das variaveis do ambiente do meu computador, vai coletar os dados para acessar o banco
load_dotenv()

usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
porta = os.getenv("PORTA")
banco = os.getenv("BANCO")

# Criando a conexão entre o banco e o código
engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}")

# Teste de conexão... 
try:
    with engine.connect() as conexao:
        print("Conexão com o banco de dados bem sucedida! ")
except Exception as e:
    print(f"A conexão falhou, erro: {e}")
    
