# Este código es un ejemplo de cómo utilizar el modelo de lenguaje "gemini-2.5-flash" de Google Generative AI para responder a una pregunta sobre la capital de Francia. El código inicializa el modelo, define la pregunta, invoca el modelo con la pregunta y luego imprime la respuesta obtenida.
from langchain_google_genai import ChatGoogleGenerativeAI

#inicializar el modelo de lenguaje
#En este caso, se está utilizando el modelo "gemini-2.5-flash" con una temperatura de 0.7 para generar respuestas más creativas.
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)
#Definir la pregunta que se le hará al modelo de lenguaje
pregunta = "¿Cuál es la capital de Francia?"
print("Pregunta:", pregunta)

#Invocar el modelo de lenguaje con la pregunta y obtener la respuesta
respuesta = llm.invoke(pregunta)
#Imprimir la respuesta del modelo
print("Respuesta del modelo", respuesta.content)
