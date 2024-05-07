import pandas as pd
from fastapi import FastAPI
from query import *
from datetime import datetime
from rotas import *
import os

app = FastAPI() # criando uma instância da classe FastAPI

@app.get("/apto_mudanca/{id_cliente_servico}/{id_cliente}") 
def verifica_apto_mudanca(id_cliente_servico,id_cliente):
    data_hoje = datetime.today().strftime('%Y-%m-%d')
    # status_servico = pd.DataFrame(consulta_servico_habilitado(id_cliente_servico))
    # status_cobranca = pd.DataFrame(consulta_cobranca_vencida(id_cliente_servico,data_hoje))
    # if status_cobranca.empty and (status_servico['prefixo'] == 'servico_habilitado').any():
    #     datas_vencimento, dados_rota = datas_vencimentos_possiveis(id_cliente)
    #     print(dados_rota)
    datas_vencimento, dados_rota = datas_vencimentos_possiveis(id_cliente_servico)
    print(dados_rota)
    if 1==1:
        resposta = {
        "status": "success",
        "msg": "Apto a mudança de vencimento",
        "grupos": "25/04/2023"  # Aqui incluímos os dados do grupo
        }
        return resposta
    else:
        return 'nao_apto'


def executa_mudanca(id_cliente_servico):
    data_hoje = datetime.today().strftime('%Y-%m-%d')
    status_servico = pd.DataFrame(consulta_servico_habilitado(id_cliente_servico))
    status_cobranca = pd.DataFrame(consulta_cobranca_vencida(id_cliente_servico,data_hoje))
    if status_cobranca.empty and (status_servico['prefixo'] == 'servico_habilitado').any():
        return 'apto'
    else:
        return 'nao_apto'
    
    # resposta = {
    # "status": "success",
    # "msg": "Dados consultados com sucesso",
    # "grupos": grupo  # Aqui incluímos os dados do grupo
    # }
    
    # # grupos_cliente_json = grupos_cliente.to_json(orient='records')
    # return resposta