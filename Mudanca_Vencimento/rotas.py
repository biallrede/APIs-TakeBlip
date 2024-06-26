import requests
from dotenv import load_dotenv
import os
import json

def datas_vencimentos_possiveis(id_cliente):
    load_dotenv()
   
    # Defina o token de autenticação Bearer
    token = os.getenv("TOKEN_TESTE")

    # Defina a URL da rota
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/cliente/servico/{id_cliente}/edit".format(id_cliente=id_cliente)
   
    # Defina o cabeçalho de autenticação
    headers = {"Authorization": f"Bearer {token}"}
  

    # Faça a solicitação GET
 
    response = requests.get(url, headers=headers)
  

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Obtenha o conteúdo da resposta como JSON
       
        dados = response.json()

        # Extrair as datas de vencimento
        datas_vencimento = [vencimento["dia_vencimento"] for vencimento in dados.get("vencimentos", [])]
        datas_vencimento = datas_vencimento.remove(5,10,15,20,25)

        return datas_vencimento
    else:
        return response.status_code
    

def gera_dados_rota(id_cliente,data_mudanca):
    load_dotenv()
    # Defina o token de autenticação Bearer
    token = os.getenv("TOKEN_TESTE")
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/cliente/servico/{id_cliente}/edit".format(id_cliente=id_cliente)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        dados = response.json()
        servicos = dados.get("servicos", [])
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
        id_vencimento_encontrado = 0
        for venc in dados["vencimentos"]:
            valor = venc["dia_vencimento"]
            if valor == data_mudanca:
                id_vencimento_encontrado = venc["id_vencimento"]
                break  # Encerra o loop após encontrar o vencimento
            # Se o vencimento não for encontrado, você pode lidar com isso aqui fora do loop
            else:
                print("Vencimento não encontrado.")
        for servico in servicos:
            id_servico = servico.get("id_servico")
            id_cliente_servico = servico.get("id_cliente_servico")
            id_servico_status = servico.get("id_servico_status")
            id_vencimento = id_vencimento_encontrado
            valor = servico.get("valor")
            data_venda = servico.get("data_venda")
            data_venda = data_venda.replace("'",'"')
            agrupamento_nota = servico.get("agrupamento_nota")
            agrupamento_fatura = servico.get("agrupamento_fatura")
            carne = servico.get("carne")
            tipo_cobranca = servico.get("tipo_cobranca")
            tipo_cobranca = tipo_cobranca.replace("'",'"')
            validade = servico.get("validade")
        forma_cobranca = dados.get("formas_cobranca")
        forma_cobranca_dict = forma_cobranca[0] if isinstance(forma_cobranca, list) and forma_cobranca else {}
        servico_tecnologia = dados.get("servico_tecnologia")
        servico_tecnologia_dict = servico_tecnologia[0] if isinstance(servico_tecnologia, list) and servico_tecnologia else {}
        grupos = dados.get("grupos", [])
        grupos_json = json.dumps(grupos).replace("'", '"')
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
            "forma_cobranca": forma_cobranca_dict,
            "servico_tecnologia": servico_tecnologia_dict,
            "grupos":grupos
        }
        return dados_rota
    else:
        return response.status_code
    
def gera_dados_atendimento(id_cliente_servico, data_mudanca):
    load_dotenv()
    # Defina o token de autenticação Bearer
    token = os.getenv("TOKEN_TESTE")
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/atendimento/iniciar"
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {token}"}
    payload = json.dumps({
                "id_cliente_servico": f"{id_cliente_servico}"
            })
    
    response = requests.post(url, headers=headers, data=payload)
   
    if response.status_code == 200:
        dados = response.json()
        id_atendimento = ''
        id_cliente_servico = ''
        descricao = ''
        nome = ''
        telefone = ''
        email = ''
        id_tipo_atendimento = ''
        id_atendimento_status = ''
        abrir_os = ''
        nome_contato = ''
        descricao_abertura = ''
        telefone_contato =  ''
        
        cliente_servico = dados['atendimento']['cliente_servico']
        nome = cliente_servico["cliente"]["nome_razaosocial"]
        id_atendimento = dados['atendimento']['id_atendimento']
        id_cliente_servico = dados['atendimento']["id_cliente_servico"]
        descricao = "Aguardando Análise"
        telefone = dados['atendimento']["telefone_contato"]
        telefone_contato = telefone
        email = dados['atendimento']["email_contato"]
        id_tipo_atendimento = 4
        id_atendimento_status = 2
        abrir_os = "false"
        nome_contato = dados['atendimento']["nome_contato"]
        descricao_abertura = f'Mudança de data vencimento para o dia {data_mudanca}\n Cliente: {nome}\n ID Cliente Serviço: {id_cliente_servico}'

        
        dados_rota = {
            "id_atendimento": id_atendimento,
            "id_cliente_servico": id_cliente_servico,
            "nome": nome,
            "telefone": telefone,
            "telefone_contato": telefone_contato,
            "email": email,
            "tipo_atendimento":{
                "id_tipo_atendimento": id_tipo_atendimento,
                "id_tipo_atendimento_pai": 'null', 
                "descricao": "Mudança de data vencimento"
            },
            "atendimento_status":
            {
                "id_atendimento_status": id_atendimento_status, 
                "descricao": descricao,
                "prefixo": "aguardando_analise"
            },
            
            "abrir_os": abrir_os,
            "nome_contato": nome_contato,
            "descricao_abertura": descricao_abertura,
            "cliente_servico": cliente_servico,
        }
        return dados_rota
    
def abre_atendimento(dados):
    load_dotenv()
    # Defina o token de autenticação Bearer
    token = os.getenv("TOKEN_TESTE")
    url = "https://api.testeallrede.hubsoft.com.br/api/v1/atendimento"
    dados_json = json.dumps(dados).replace("'", '"')
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {token}"}
    
    
    response = requests.post(url, headers=headers, data=dados_json)
   
    return response.text