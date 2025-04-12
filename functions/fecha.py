import pandas as pd

def fecha_formateada(df, fecha):
    df[fecha] = pd.to_datetime(df[fecha], format='%d/%m/%Y')
    return df