import pandas as pd
import unicodedata

# Función para eliminar tildes
def remover_tildes(texto):
    if pd.isnull(texto):
        return texto
    texto = str(texto)
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')

# Función para estandarizar texto
def estandarizar_texto(df, columnas=None):
    """
    Estandariza texto en columnas: quita tildes, strip, lower y reemplazo de espacios múltiples.
    
    Parámetros:
    - df: DataFrame.
    - columnas: Lista de columnas a estandarizar. Si None, aplica a todas tipo object/string.
    
    Retorna:
    - df limpio.
    """
    if columnas is None:
        columnas = df.select_dtypes(include=['object', 'string']).columns

    # Procesa cada columna de texto seleccionada
    for col in columnas:
        df[col] = (
            df[col]
            .apply(remover_tildes)                  # Elimina tildes
            .str.strip()                            # Quita espacios al principio y final
            .str.lower()                            # Pasa a minúsculas
            .str.replace(r'\s+', ' ', regex=True)   # Reemplaza espacios múltiples por uno solo
        )
    
    return df