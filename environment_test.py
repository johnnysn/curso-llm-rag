from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def main():
    messages = []

    model = Ollama(model="llama3.1")

    while True:
        user_input = input("Pergunta (escreva 'quit' para sair): ")

        if user_input.lower() == "quit":
            print("Até mais!")
            break

        messages.append(("human", user_input))

        prompt = ChatPromptTemplate.from_messages(messages)
        parser = StrOutputParser()

        chain = prompt | model | parser
        chunks = chain.stream({})

        response = ""
        for chunk in chunks:
            print(chunk, end="", flush=True)
            response += chunk
        print()

        messages.append(("ai", response))


if __name__ == "__main__":
    main()
