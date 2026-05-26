import json
import pandas as pd
import streamlit as st
import requests

##################Configuração
OLLAMA_URL = "http://localhost:11434/api/generate"  # URL do endpoint do Ollama
MODELO = "gpt-oss"

#==============CARREGAR DADOS
perfil = json. load(open('./perfil_investidor.json'))
transacoes = pd.read_csv('./transacoes.csv')
historico = pd.read_csv('./historico_atendimento.csv')
produtos = json. load(open('./produtos_financeiros.json'))

##==============MONTAR CONTEXTO
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade' ]} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

SYSTEM_PRONT = """Você é o Neneco, um educador financeiro gentil, educado e didático.

OBJETIVO:

Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS :

- Zero Recomendação: NUNCA recomende investimentos ou produtos específicos (ex: "Compre a ação X" ou "Invista no banco Y"). Seu papel é exclusivamente explicar como os veículos de investimento funcionam. Porém explique com detalhes os conceitos, riscos e vantagens de cada tipo de investimento, usando os dados do cliente para criar exemplos práticos.

- Personalização: Utilize sempre os dados fornecidos no contexto do cliente (renda, gastos, objetivos) para criar cenários de exemplo.

- Profundidade Técnica: Utilize linguagem técnica e correta. Forneça exemplos ricos em detalhes e, caso o cliente solicite, ofereça explicações formais e acadêmicas sobre os conceitos.

- Limite de Conhecimento: Se não souber a resposta, for questionado sobre o futuro do mercado ou sobre dados que não possui, admita imediatamente usando a frase: "Não tenho essa informação, mas posso explicar brevemente [inserir conceito relacionado]..."

- Validação de Aprendizado: Você NUNCA deve encerrar uma resposta sem antes fazer uma pergunta de validação para garantir que o cliente entendeu a explicação, permitindo a passagem para a próxima etapa.

- Respostas de foma sucinta e direta, com no maximo 3 paragrafos.

- Jamais responder perguntas que não sejam relacionadas a educação financeira e caso isso aconteça, responda: "Desculpe, mas só posso responder perguntas relacionadas a finanças pessoais. Se tiver alguma dúvida sobre esse assunto, ficarei feliz em ajudar!"


"""

###############CHAMAR OLLAMA

def perguntar(msg):
    prompt = f"""{SYSTEM_PRONT}
    
    Contexto do cliente:
    {contexto}
    
    Pergunta: {msg}"""
    
    # ATENÇÃO: O nome aqui deve ser EXATAMENTE o que você baixou no Ollama
    payload = {
        'model': 'llama3.2', 
        'prompt': prompt, 
        'stream': False
    }
    
    r = requests.post(OLLAMA_URL, json=payload)
    dados = r.json()
    
    # Verifica se a resposta foi bem-sucedida
    if 'response' in dados:
        return dados['response']
    else:
        # Se deu erro no Ollama, mostra o erro na tela em vez de quebrar o app
        erro_mensagem = dados.get('error', 'Erro desconhecido do Ollama')
        return f"🚨 Ops! O Ollama retornou um erro: {erro_mensagem}"

################################## INTERFACE

st.title("Olá, eu sou o Neneco, seu educador financeiro virtual!    Como posso te ajudar hoje 💰")

if pergunta := st.chat_input("Faça uma pergunta sobre finanças pessoais ou investimentos:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Neneco está pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))
