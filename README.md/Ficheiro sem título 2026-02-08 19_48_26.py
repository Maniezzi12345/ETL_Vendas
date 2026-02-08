# 📊 Projeto de Pipeline de Vendas - Loja X

## 📌 Objetivo
Construir um pipeline de dados para análise de desempenho da Loja X, utilizando a arquitetura **Medallion (Bronze, Prata e Ouro)**, integrando dados de diferentes fontes e disponibilizando dashboards no Power BI para acompanhamento de métricas de vendas.

---

## ⚙️ Tecnologias Utilizadas
- **Banco de Dados:** PostgreSQL  
- **ETL/Orquestração:** Databricks (via ODBC)  
- **Armazenamento e Catálogo:** Azure Data Lake + Unity Catalog  
- **Visualização:** Power BI  
- **Cloud Provider:** Microsoft Azure  

---

## 🏛️ Arquitetura Medallion
- **Bronze:**  
  - Dados brutos importados de arquivos CSV vindos do PostgreSQL.  
  - Nenhuma transformação aplicada, apenas ingestão.  

- **Prata:**  
  - Limpeza e padronização dos dados.  
  - Tratamento de valores nulos, duplicados e normalização de colunas.  

- **Ouro:**  
  - Dados prontos para consumo analítico.  
  - Aplicação da **arquitetura estrela (Star Schema)** para relacionar tabelas fato e dimensões.  
  - Exemplo:  
    - **Fato:** Itens_pedido
    - **Dimensões:** Clientes, Produtos, Pedidos, Calendário

---

## 📈 Métricas Disponibilizadas no Dashboard
- Total de clientes  
- Valor da receita  
- Ticket médio  
- Total de pedidos  
- Clientes por município  
- Vendas por produto  
- Evolução de vendas por período (linha temporal)  

---

## 🔄 Orquestração
- Criação de **notebooks no Databricks** para cada etapa (Bronze → Prata → Ouro).  
- Configuração de **Job Pipeline** para execução automatizada.  
- Envio dos dados tratados para o **Power BI**.  

