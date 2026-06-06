# Esta importacion es necesaria para utilizar la clase ChatOpenAI, que permite interactuar con el modelo de lenguaje GPT-4o-mini. En este ejemplo, se utiliza ChatOpenAI para generar un saludo creativo basado en una plantilla de prompt.
from langchain_openai import ChatOpenAI

# Esta importacion es necesaria para utilizar la clase PromptTemplate, que permite definir plantillas de texto con variables de entrada que se pueden utilizar para generar prompts personalizados para el modelo de lenguaje. En este ejemplo, se utiliza PromptTemplate para crear una plantilla de saludo que incluye una variable de entrada "nombre".
from langchain.prompts import PromptTemplate

# Esta importacion es necesaria para utilizar la clase LLMChain, que permite encadenar múltiples pasos de procesamiento utilizando un modelo de lenguaje. En este ejemplo, no se utiliza LLMChain, pero se importa para mostrar cómo se podría utilizar en casos más complejos donde se necesiten múltiples pasos de procesamiento.
from langchain.chains import LLMChain

# Inicializar el modelo de lenguaje
chat = ChatOpenAI(model="gpt-4o-mini",temperature=0.7)

# Definir la plantilla de prompt con una variable de entrada "nombre". La plantilla solicita al modelo que salude a la persona de manera creativa.
plantilla = PromptTemplate(
    # Definir la variable de entrada "nombre" que se utilizará en la plantilla.
    input_variables=["nombre"],
    # Definir el texto de la plantilla que se le dará al modelo. El texto incluye un espacio para insertar el valor de la variable "nombre".
    template="Saluda al usuario con su nombre. Nombre del usuario : {nombre}.\nAsistente : "
)

# Crear una cadena de procesamiento utilizando LLMChain, que toma el modelo de lenguaje y la plantilla de prompt como entrada. La cadena se puede ejecutar con diferentes valores para la variable "nombre" para generar saludos personalizados.
chain =  LLMChain(llm=chat, prompt=plantilla)

# Ejecutar la cadena de procesamiento con un valor específico para la variable "nombre". En este caso, se le pide al modelo que salude a "Juan". El resultado será un saludo creativo generado por el modelo de lenguaje.
resultado = chain.run(nombre="Juan")

# Imprimir el resultado del saludo generado por el modelo de lenguaje.
print(resultado)