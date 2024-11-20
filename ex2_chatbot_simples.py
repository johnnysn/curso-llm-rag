from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

mensagens = []
instructions = """Você é um assistente de inteligência artificial que ajuda os usuários a responder perguntas 
e a resolver problemas.
"""

llm = ChatOllama(model="llama3.2", temperature=0.01)
parser = StrOutputParser()


while True:
    pergunta = input("Pergunta (ou 's' para sair): ")

    if pergunta == "s":
        break

    # Cria um prompt com as mensagens atuais
    prompt = ChatPromptTemplate.from_messages(
        [("system", instructions), ("human", pergunta)]
    )

    # Cria uma chain para processar a resposta
    chain = prompt | llm | parser

    # Obtém resposta da chain via streaming
    response_stream = chain.stream({})

    print("Resposta: ", end="")
    for chunk in response_stream:
        print(chunk, end="", flush=True)
    print()
