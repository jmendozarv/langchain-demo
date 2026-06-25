from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Eres un asistente util que mantiene el contexto de la conversacion.")
        MessagesPlaceholder(variable_name="historial"),
        ("human", "Usuario:{pregunta_actual}")
    ]
)

# Simulamos un historial de conversacion
historial_conversacion = [
    HumanMessage(content="Usuario : Cual es la capital de Francia?"),
    AIMessage(content="IA : La capital de Francia"),
    HumanMessage(content="Usuario : Y cuantos habitantes tiene?"),
    AIMessage(content="IA : Tiene aproximadamente 2.1 millones de habitantes.")
]

mensajes = chat_prompt.format_messages(
    historial = historial_conversacion,
    pregunta_actual = "Puedes decirme algo interesante de su arquitectura?"
)

for mensaje in mensajes:
    print(f"{mensaje.type}: {mensaje.content}")