from langchain_openai import OpenAI, ChatOpenAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

def crear_evaluador_cv() -> AnalisisCV:
    modelo_base = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.2
    )
    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompts = crear_sistema_prompts()
    return chat_prompts | modelo_estructurado

def evaluar_candidato(texto_cv : str, descripcion_puesto:str)-> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })
        return resultado
    except Exception as e:
        return AnalisisCV(
            nombre_candidato="Error al procesar el CV",
            experiencia_anos=0,
            habilidades_clave=["Error"],
            educacion="Error",
            experiencia_relevante="Error durante el analisis.",
            fortalezas=["Error durante el analisis."],
            areas_mejora=["Error durante el analisis."],
            porcentaje_ajuste= 0
        )


