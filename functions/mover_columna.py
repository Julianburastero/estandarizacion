def mover_columna(df, columna, nueva_posicion):
    # Obtiene el orden actual de las columnas
    cols = list(df.columns)
    
    # Quita la columna que deseas mover
    cols.remove(columna)
    
    # Inserta la columna en la nueva posición
    cols.insert(nueva_posicion, columna)
    
    # Reorganiza las columnas en el DataFrame
    return df[cols]
