import requests
from dotenv import load_dotenv
import os
import json

def datas_vencimentos_possiveis(id_cliente):
    load_dotenv()
    print("entrei na rota")
    # Defina o token de autenticação Bearer
    token = os.getenv("TOKEN_TESTE")

    # Defina a URL da rota
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/cliente/servico/{id_cliente}/edit".format(id_cliente=id_cliente)
    print("montei a url: ",url)
    # Defina o cabeçalho de autenticação
    headers = {"Authorization": f"Bearer {token}"}
    print("monetei o bearer token: ",token)

    # Faça a solicitação GET
    print("preparando a requisição")
    response = requests.get(url, headers=headers)
    print("requisição feita")

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Obtenha o conteúdo da resposta como JSON
        print("lendo json")
        dados = response.json()

        # Extrair as datas de vencimento
        datas_vencimento = [vencimento["dia_vencimento"] for vencimento in dados.get("vencimentos", [])]
        servicos = dados.get("servicos", [])
        # print(servicos)
        id_servico = ''
        id_cliente_servico = ''
        id_servico_status = ''
        id_vencimento = ''
        valor = ''
        data_venda = ''
        data_venda = ''
        agrupamento_nota = ''
        agrupamento_fatura = ''
        carne = ''
        tipo_cobranca = ''
        tipo_cobranca = ''
        validade = ''
        # print('aquiiiiiiiiiiiiiiiiiiiiiiii')
        # print(servicos)
        for servico in servicos:
            # print('entreiiiiiiii')
            id_servico = servico.get("id_servico")
            # print("id_servicoooooo: ",id_servico)
            id_cliente_servico = servico.get("id_cliente_servico")
            id_servico_status = servico.get("id_servico_status")
            id_vencimento = servico.get("id_vencimento")
            valor = servico.get("valor")
            data_venda = servico.get("data_venda")
            data_venda = data_venda.replace("'",'"')
            agrupamento_nota = servico.get("agrupamento_nota")
            agrupamento_fatura = servico.get("agrupamento_fatura")
            carne = servico.get("carne")
            tipo_cobranca = servico.get("tipo_cobranca")
            tipo_cobranca = tipo_cobranca.replace("'",'"')
            validade = servico.get("validade")
        forma_cobranca = dados.get("formas_cobranca", {})
        forma_cobranca_json = json.dumps(forma_cobranca)
        forma_cobranca_json = forma_cobranca_json.replace("'",'"')
        servico_tecnologia = dados.get("servico_tecnologia", {})
        servico_tecnologia_json = json.dumps(servico_tecnologia)
        servico_tecnologia_json = servico_tecnologia_json.replace("'",'"')
        dados_rota = {
            "id_servico": id_servico,
            "id_cliente_servico": id_cliente_servico,
            "id_servico_status": id_servico_status,
            "id_vencimento": id_vencimento,
            "valor": valor,
            "data_venda": data_venda,
            "agrupamento_nota": agrupamento_nota,
            "agrupamento_fatura": agrupamento_fatura,
            "carne": carne,
            "tipo_cobranca": tipo_cobranca,
            "validade": validade,
            "forma_cobranca": forma_cobranca,
            "servico_tecnologia": servico_tecnologia
        }

        dados_rota = json.dumps(dados_rota)
        # Exibir as datas de vencimento
        # print("Datas de Vencimento:")
        # for data in datas_vencimento:
        #     print(data)

        return datas_vencimento,dados_rota
    else:
        print("Falha na solicitação. Código de status:", response.status_code)

