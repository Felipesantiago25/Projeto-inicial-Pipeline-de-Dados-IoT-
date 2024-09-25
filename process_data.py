import pandas as pd

# Caminho para o arquivo CSV
csv_file_path = 'C:\Users\emphasys.felipe\venv\IOT-temp.csv'

# Leitura do arquivo CSV
try:
    df = pd.read_csv(csv_file_path)
    print("Dados carregados com sucesso:")
    print(df.head())  # Exibe as primeiras linhas do DataFrame
except FileNotFoundError:
    print(f"Arquivo não encontrado: {csv_file_path}")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")

# Processamento básico de dados (exemplo)
# Verifique se o DataFrame contém as colunas esperadas
if 'device_id' in df.columns and 'temperature' in df.columns:
    print("Colunas encontradas no CSV:")
    print(df.columns)
else:
    print("Colunas esperadas não encontradas no arquivo CSV.")
