# Construção de Chatbots com RAG: Extraindo Conhecimento de Documentos e da Web

Este projeto contém exemplos didáticos utilizando [LangChain](https://www.langchain.com/) para a criação de aplicações com LLMs e RAG.

## Pré-requisitos

É necessário ter o [Ollama](https://ollama.com) instalado previamente, com os modelos `llama3.2` e `nomic-embed-text` baixados. 

## Configuração do ambiente

### 1. Instalar dependências essenciais

Primeiro, certifique-se de que as ferramentas básicas para o desenvolvimento Python estejam instaladas:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

### 2. Clonar este repositório

Clone o repositório com o código do projeto:

```bash
git clone https://github.com/johnnysn/curso-llm-rag.git
cd curso-llm-rag
```

### 3. Criar e ativar um ambiente virtual

Para isolar as dependências do projeto, crie e ative um ambiente virtual Python:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar as dependências do projeto

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Iniciar o Jupyter Notebook

Agora, você pode iniciar o Jupyter Notebook para acessar e executar os notebooks do projeto:

```bash
jupyter notebook
```

O Jupyter irá abrir uma interface no navegador. A partir dela, você pode navegar até os notebooks do projeto e executá-los.


### 6. Links úteis

- [Canal do Youtube sobre Ollama e LLMs locais](https://www.youtube.com/@technovangelist)
- [Web UI local para conversar com LLMs instaladas no Ollama](https://github.com/open-webui/open-webui)
- [Construindo interfaces web para suas aplicações com Streamlit](https://www.youtube.com/watch?v=ZHZKPmzlBUY)