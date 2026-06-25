from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    """Modelo de datos para el analisis completo de un CV"""
    nombre_candidato:str = Field(description="Nombre completo candidato extraido del CV.")
    experiencia_anos: int = Field(description="Años de experiencia laboral del candidato extraido del CV.")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 habilidades clave del candidato extraido del CV.")
    educacion: str = Field(description="Nivel educativo del candidato extraido del CV.")
    experiencia_relevante:str  = Field(description="Resumen conciso de la experiencia mas relevante para el puesto especifico.")
    fortalezas: list[str] = Field(description="3-5 princicpales fortalezas del candidato basadas en su perfil.")
    areas_mejora: list[str] = Field(description="2-4 areas donde le candidato podria desarrollarse o mejorar.")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste al puesto(0-100) basado en la experiencia , habilidades y formacion.",ge=0,le=100)
