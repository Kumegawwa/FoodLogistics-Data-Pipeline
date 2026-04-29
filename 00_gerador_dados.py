import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')

# 1. Gerando Clientes
clientes = [{'ID_Cliente': i, 'Nome': fake.name(), 'Estado': fake.state_abbr(), 'Cidade': fake.city()} for i in range(1, 101)]
pd.DataFrame(clientes).to_csv('clientes.csv', index=False)

# 2. Gerando Produtos
categorias = ['Congelados', 'Laticínios', 'Carnes', 'Hortifruti']
produtos = [{'ID_Produto': i, 'Nome': fake.word().capitalize(), 'Categoria': random.choice(categorias), 'Preco': round(random.uniform(10.0, 150.0), 2)} for i in range(1, 51)]
pd.DataFrame(produtos).to_csv('produtos.csv', index=False)

# 3. Gerando Vendas/Logística
status = ['Entregue', 'Atrasado', 'Cancelado']
vendas = []
for i in range(1, 1001):
    data_venda = fake.date_between(start_date='-1y', end_date='today')
    vendas.append({
        'ID_Venda': i,
        'ID_Cliente': random.randint(1, 100),
        'ID_Produto': random.randint(1, 50),
        'Data_Venda': data_venda,
        'Status_Entrega': random.choices(status, weights=[70, 20, 10])[0],
        'Custo_Frete': round(random.uniform(15.0, 80.0), 2)
    })
pd.DataFrame(vendas).to_csv('vendas_logistica.csv', index=False)

print("Arquivos CSV gerados com sucesso!")