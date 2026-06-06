# Este código es un ejemplo de cómo utilizar el modelo de lenguaje GPT-4 para responder a una pregunta sobre la capital de Francia.
from langchain_openai import ChatOpenAI

#inicializar el modelo de lenguaje
#En este caso, se está utilizando el modelo "gpt4o-mini" con una temperatura de 0.7 para generar respuestas más creativas.
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
#Definir la pregunta que se le hará al modelo de lenguaje
pregunta = "¿Cuál es la capital de Francia?"
print("Pregunta:", pregunta)

#Invocar el modelo de lenguaje con la pregunta y obtener la respuesta
respuesta = llm.invoke(pregunta)
#Imprimir la respuesta del modelo
print("Respuesta del modelo", respuesta.content)
