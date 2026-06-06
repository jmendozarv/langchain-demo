## importando dependencias
from langchain_openai import ChatOpenAI
# Esta importacion es necesaria para utilizar la clase PromptTemplate, que permite definir plantillas de texto con variables de entrada que se pueden utilizar para generar prompts personalizados para el modelo de lenguaje. En este ejemplo, se utiliza PromptTemplate para crear una plantilla de saludo que incluye una variable de entrada "nombre".
from langchain.schema import AIMessage , HumanMessage , SystemMessage

import streamlit as st

# Configurar la pagina de la app
st.set_page_config(page_title="Chatbot Basico",page_icon="🤖")
st.title("🤖Chatbot Basico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain y Streamlit. Escribe un mensaje y el chatbot te responderá.")


chat_model  = ChatOpenAI(model="gpt-4o-mini",temperature=0.5)

## grado de memoria para seguir la convesacion
## Inicializar historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


## Mostrar mensajes previos
for msg in st.session_state.mensajes:
    if isinstance(msg,SystemMessage):
        # No muestro los mensajes del sistema
        continue
    role = "assistant" if isinstance(msg,AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

# Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje : ")

if pregunta:
    # Mostrar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Almacenar el mensaje del usuario en el historial de streamlit
    st.session_state.mensajes.append(HumanMessage(content=pregunta))

    # Generar respuesta del chatbot utilizando el modelo de lenguaje
    respuesta = chat_model.invoke(st.session_state.mensajes)

    # Mostrar la respuesta en la interfaz
    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    st.session_state.mensajes.append(respuesta)


