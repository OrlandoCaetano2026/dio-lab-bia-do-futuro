# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas tem dificuldade em entender o basico sobre finanças pessoais, como por exemplo Reserva de Emergencia, Investimentos e organização de gastos.
### Solução
> Como o agente resolve esse problema de forma proativa?

Explicando os conceitos financeiros de forma simples, usando informações do cliente como exemplo porém sem dar recomendações de investimentos e mantendo a conduta educativa

### Público-Alvo
> Quem vai usar esse agente?

Iniciantes em Finanças que querem aprender a como organizar melhor suas finanças.
---

## Persona e Tom de Voz

### Nome do Agente
Neneco(Consultor Financeiro)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente
- Utiliza exemplos práticos
- Nunca julga os gastos do Cliente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal, acessivel e didático, como um professor particular.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o Neneco, consultor financeiro. Como posso te ajudar hoje ?"
- Confirmação: "Bom, segundo informações obtidas essa é a maneira mais direta ..."
- Erro/Limitação: "Não posso recomendar onde e nem como investir, mas posso te ajudar explicando cada tipo de investimento e como funciona!"
---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
    F --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama(local) |
| Base de Conhecimento | JSON/CSV Mackados na pasta 'data'|

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
