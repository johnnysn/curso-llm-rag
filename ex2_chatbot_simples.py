from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

instructions = """Você é um assistente de inteligência artificial que ajuda os usuários a responder perguntas 
e a resolver problemas.
"""

llm = ChatOllama(model="llama3.2", temperature=0.01)
parser = StrOutputParser()

mensagens = [("system", instructions)]

while True:
    pergunta = input("Pergunta (ou 's' para sair): ")

    if pergunta == "s":
        break

    # Adiciona pergunta ao histórico de mensagens
    mensagens.append(("user", pergunta))

    # Cria um prompt com as mensagens atuais
    prompt = ChatPromptTemplate.from_messages(mensagens)

    # Cria uma chain para processar a resposta
    chain = prompt | llm | parser

    # Obtém resposta da chain via streaming
    response_stream = chain.stream({})
    resposta = ""

    print("Resposta: ", end="")
    for chunk in response_stream:
        resposta += chunk
        print(chunk, end="", flush=True)
    print()

    # Salva resposta do modelo no histórico de mensagens
    mensagens.append(("ai", resposta))
