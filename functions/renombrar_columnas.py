def renombrar_cols(df, diccionario_nombres):
    df = df.rename(columns=diccionario_nombres)
    return df