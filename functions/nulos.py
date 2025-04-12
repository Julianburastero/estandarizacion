import pandas as pd

def tratar_nulos(df, reglas):
    """
    Trata los valores nulos de un DataFrame según reglas personalizadas para cada columna.
    
    Parámetros:
    - df: DataFrame con datos a tratar.
    - reglas: Diccionario con las reglas de tratamiento para cada columna.
    
    Las claves del diccionario son los nombres de las columnas, y los valores son los métodos de tratamiento a aplicar.
    Los métodos de tratamiento pueden ser:
    - 'eliminar': Eliminar filas con nulos en esta columna.
    - 'rellenar_0': Rellenar los nulos con 0.
    - 'rellenar_media': Rellenar los nulos con la media de la columna.
    - 'rellenar_median': Rellenar los nulos con la mediana de la columna.
    - 'rellenar_con': Rellenar los nulos con un valor específico (proporcionado en el diccionario).
    
    Devuelve el DataFrame con los nulos tratados.
    """
    for columna, metodo in reglas.items():
        if metodo == 'eliminar':
            # Eliminar filas con valores nulos en la columna
            df = df.dropna(subset=[columna])
        elif metodo == 'rellenar_0':
            # Rellenar los nulos con 0
            df[columna] = df[columna].fillna(0)
        elif metodo == 'rellenar_media':
            # Rellenar los nulos con la media de la columna
            df[columna] = df[columna].fillna(df[columna].mean())
        elif metodo == 'rellenar_median':
            # Rellenar los nulos con la mediana de la columna
            df[columna] = df[columna].fillna(df[columna].median())
        elif isinstance(metodo, (int, float, str)):
            # Rellenar con un valor específico
            df[columna] = df[columna].fillna(metodo)
        else:
            print(f"Regla desconocida para la columna '{columna}': {metodo}")
    
    return df
