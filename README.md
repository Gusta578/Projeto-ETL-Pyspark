# Projeto ETL de Transações com PySpark

## Descrição

Este projeto implementa um pipeline de dados para processar informações de transações financeiras, seguindo a arquitetura de Data Lake com as camadas Bronze, Silver e Gold.  
Utiliza PySpark para tratamento e agregação dos dados e exporta os resultados para um banco MySQL.

## Tecnologias utilizadas

- Python 3.x  
- PySpark  
- Pandas  
- MySQL  
- SQLAlchemy  
- Apache Airflow (planejado para orquestração)  
- Git/GitHub (controle de versão)

## Estrutura do projeto

- `scripts/etl.py`: Pipeline ETL completo do Bronze ao Gold  
- `database.py`: Configuração da conexão com o banco MySQL  
- `dados/bronze/`: Dados originais (CSV)  
- `dados/silver/`: Dados tratados  
- `dados/gold/`: Dados agregados  
- `.env`: Variáveis de ambiente com credenciais do banco  

## Como executar

1. Clone o repositório  
2. Configure o arquivo `.env` com as credenciais do banco MySQL  
3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
