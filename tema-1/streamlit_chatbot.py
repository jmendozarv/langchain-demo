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


