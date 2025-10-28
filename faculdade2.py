import sqlite3

# Conectar ao banco de dados (ou criar)
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Inserir dados
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

conexao.commit()
import pandas as pd

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas.head()
# Verificar estatísticas básicas
print(df_vendas.describe())

# Total de vendas por categoria
print(df_vendas.groupby('categoria')['valor_venda'].sum())

# Vendas por mês
df_vendas['mes'] = df_vendas['data_venda'].dt.month
print(df_vendas.groupby('mes')['valor_venda'].sum())
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de barras - Vendas por categoria
plt.figure(figsize=(8, 5))
sns.barplot(data=df_vendas, x='categoria', y='valor_venda', estimator=sum)
plt.title('Total de Vendas por Categoria')
plt.ylabel('Valor em R$')
plt.xlabel('Categoria')
plt.show()

# Gráfico de linha - Vendas ao longo do tempo
df_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_mes, x='mes', y='valor_venda', marker='o')
plt.title('Vendas Mensais em 2023')
plt.xlabel('Mês')
plt.ylabel('Valor Total de Vendas')
plt.xticks(range(1,13))
plt.grid()
plt.show()
