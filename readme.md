# Projeto de Pipeline de Dados IoT

Este projeto visa criar um pipeline de dados para processar, armazenar e visualizar dados de temperatura coletados por dispositivos IoT. Ele utiliza o PostgreSQL como banco de dados para armazenar as leituras e o **Streamlit** para criar um dashboard interativo com gráficos que representam os dados.

## Estrutura do Projeto

1. **Configuração do Ambiente**
   - Instalação do Python.
   - Instalação do Docker.
   - Criação de um contêiner PostgreSQL usando Docker.
   - Criação de um ambiente virtual Python e instalação de bibliotecas necessárias.

2. **Processamento e Inserção de Dados**
   - Script Python para ler um arquivo CSV com leituras de temperatura e inserir os dados no banco de dados PostgreSQL.
   - Utilização de **SQLAlchemy** para conectar ao banco de dados PostgreSQL.
   
3. **Visualização dos Dados**
   - Criação de um dashboard interativo usando **Streamlit** para visualizar as leituras de temperatura, com gráficos e insights.
   - Definição de três views SQL para representar dados agregados, como a média de temperatura por dispositivo, temperatura máxima e mínima por dia, e a contagem de leituras por hora.

## 1. Configuração do Ambiente

### Instalação de Dependências

Certifique-se de ter o Python instalado. Depois, siga estas etapas:

1. **Instalar o Docker**:
   - Siga as instruções no [site oficial do Docker](https://docs.docker.com/get-docker/) para instalar Docker.

2. **Criar o ambiente virtual e instalar bibliotecas necessárias**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   pip install pandas psycopg2-binary sqlalchemy streamlit plotly
