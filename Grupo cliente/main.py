import pandas as pd
from fastapi import FastAPI
from query import consulta_cliente

app = FastAPI() # criando uma instância da classe FastAPI

@app.get("/grupos_cliente/{cpf_cnpj}/{id_cliente_servico}") 
def consulta_grupos_cliente(cpf_cnpj,id_cliente_servico):
    grupos_cliente = consulta_cliente(cpf_cnpj,id_cliente_servico)
    grupos_cliente_json = grupos_cliente.to_json(orient='records')
    return grupos_cliente_json
