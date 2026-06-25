from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Eres un traductor del español al ingles muy preciso."),
        ("human", "Traduce el siguiente texto: {texto}")
    ]
)

mensajes = chat_prompt.format_messages(texto = "Hola mundo,¿cómo estás?")

for mensaje in mensajes:
    print(f"{mensaje.type}: {mensaje.content}")