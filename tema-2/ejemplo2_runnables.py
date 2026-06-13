# 1. Configuracion inicial
from langchain_core.runnables import RunnableLambda , RunnableParallel
from langchain_openai import ChatOpenAI
import json

# Configuracion del modelo
llm = ChatOpenAI(model= "gpt-4o-mini" , temperature=0)

# Pregunta reflexiva: ¿Por qué usamos temperature=0 para análisis de sentimientos?
# Usamos temperature=0 para análisis de sentimientos porque queremos obtener respuestas más determinísticas y consistentes.
# Al establecer la temperatura en 0, el modelo tiende a generar respuestas más predecibles y menos creativas,
# lo que es ideal para tareas como el análisis de sentimientos donde buscamos una interpretación clara y objetiva del texto.

# 2. Preprocesador de Texto
def reprocess_text(text):
    """Limpia el texto eliminando espacios extras y limitando longitud"""
    # Pista: usa .strip() para eliminar espacios
    # Pista: limita a 500 caracteres con slicing [:500]
    return text.strip()[:500]

# Convertir la funcion en un Runnable
reprocessor  = RunnableLambda(reprocess_text)

# 3. Generador de Resumenes
# Objetivo: Crear una función que genere un resumen conciso del texto.
def generate_summary(text):
    """Genera un resumen conciso del texto"""
    prompt = f"""
Eres un asistente experto en resumen en español.
Resume el siguiente texto en EXACTAMENTE una sola oración.

Reglas:
- Máximo 25 palabras.
- Conserva la idea principal y el resultado clave.
- No inventes datos ni añadas opiniones.
- Evita ejemplos y detalles secundarios.
- Si el texto ya es muy breve, reformúlalo con claridad sin perder significado.

Texto: 
\"\"\"{text}\"\"\"

Devuelve solo la oración final.
"""
    response = llm.invoke(prompt)
    return response.content.strip()

## Reto: ¿Podrías mejorar este prompt para obtener mejores resúmenes?


summary_branch = RunnableLambda(generate_summary)


# 4. Analizador de sentimientos
# Crear una función que analice el sentimiento y devuelva JSON estructurado.

def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado"""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}

    Texto: {text}"""

    response = llm.invoke(prompt)
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}

# ¿Por qué es importante el manejo de errores con try/except aquí?
# Es importante manejar errores con try/except al analizar el sentimiento porque el modelo de
# lenguaje podría no siempre devolver un JSON válido, lo que podría causar que el programa falle.
# Al usar try/except, podemos capturar cualquier error de decodificación JSON y proporcionar
# una respuesta predeterminada o una justificación en caso de que el análisis falle,
# asegurando que el programa continúe funcionando sin interrupciones.


sentiment_branch = RunnableLambda(analyze_sentiment)


# 5. Función de Combinación
#
# Objetivo: Unificar los resultados de resumen y análisis de sentimientos.

def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

merger_results = RunnableLambda(merge_results)

parallel_analysis = RunnableParallel({
    "resumen": summary_branch,
    "sentimiento": summary_branch,
})


# 7. Construcción de la Cadena Final
#
# Objetivo: Conectar todos los componentes usando LCEL.

# La cadena completa
chain = reprocessor | parallel_analysis | merger_results

review_batch = [
    "EXcelente producto , muy satisfecho con la compra",
    "Terrible calidad , no lo recomiendo para nada",
    "Esta bien , cumple su funcion basica pero nada especial"
]

resultado_batch = chain.batch(review_batch)

print(resultado_batch)