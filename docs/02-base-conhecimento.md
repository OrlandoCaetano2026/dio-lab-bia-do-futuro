# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, tem o reconhecimento do cliente de forma mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar explicações e duvidas sobre as necessidades do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponiveis para que eles possam ser ensinados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e utilizar a informação de forma didatica |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O fundo  multimercado foi substituido pelo produto imobiliário (FII), pois o produto financeiro é mais conhecido assim garanto a validação de resposta mais acertivas
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

'''python
import pandas as pd
import json

# CSVs
historico = pd.read_cvs('data/historico_atendimento')
transacoes = pf.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', "r", encoding= 'utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding= 'utf-8') as f:
  produtos = json.load(f)
'''
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
