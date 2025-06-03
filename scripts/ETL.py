from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from database import engine

spark = SparkSession.builder.appName("ProjetoETLTransacoes").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("dados\\bronze\\transacoes.csv")

# Limpeza dos dados, remover valores nulos, formatação da coluna e criação de nova coluna chamada "valor com taxa"
df_silver = df.dropna(subset=["id", "cliente", "data", "valor", "categoria"])
df_silver = df_silver.withColumn("data", to_date(col("data"), "yyyy-MM-dd"))
df_silver = df_silver.withColumn("valor_com_taxa", col("valor") * 1.05)

# Enviando o dataframe para o pandas para ficar mais facil de enviar para a pasta silver
df_silver_pd = df_silver.toPandas()
df_silver_pd.to_csv("dados/silver/transacoes_silver.csv", index=False)

# Gerando insights a partir dos dados tratados do silver para saber o total gasto pelo cliente em cada categoria
df_gold = df_silver.groupBy("cliente", "categoria").sum("valor") \
    .withColumnRenamed("sum(valor)", "total_gasto")

# Enfim enviando para a pasta Gold do meu datalake
df_gold_pd = df_gold.toPandas()
df_gold_pd.to_csv("dados/gold/transacoes_gold.csv", index=False)

# Enviando o dataframe para o banco de dados
df_gold_pd.to_sql("transacoes_gold", con=engine, if_exists="replace", index=False)



