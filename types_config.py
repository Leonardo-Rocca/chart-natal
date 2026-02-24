from typing import TypedDict

class Fondo(TypedDict):
    id: str      # Un identificador único (slug)
    name: str    # Nombre para mostrar en la UI
    path: str    # Ruta al archivo
    color: str   # Color de fuente (white/black)
    name_font: str    # Fuente del nombre
    subname_font: str # Fuente de la fecha/subtítulo