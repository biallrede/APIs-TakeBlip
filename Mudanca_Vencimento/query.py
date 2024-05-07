import pandas as pd 
from credentials import credenciais_banco

def consulta_servico_habilitado(id_cliente_servico):
    conn = credenciais_banco()   
    query = '''
                select a.id_cliente_servico, b.prefixo from cliente_servico a
                left join servico_status b on a.id_servico_status = b.id_servico_status
                where a.id_cliente_servico = {id_cliente_servico}

                    '''.format(id_cliente_servico=id_cliente_servico)
        
    df = pd.read_sql(query,conn)
    return df

def consulta_cobranca_vencida(id_cliente_servico,data):
    conn = credenciais_banco()   
    query = '''
                select * from cobranca 
                where id_cliente_servico = {id_cliente_servico}
                and data_vencimento < '{data_hoje}'
                and status = 'vencido'

                    '''.format(id_cliente_servico=id_cliente_servico, data_hoje=data)
        
    df = pd.read_sql(query,conn)
    return df