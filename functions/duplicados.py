import pandas as pd

def duplicados_f(df, subset=None):

    #Agregar documentación

    clean_df = df.drop_duplicates(subset = None)

    return clean_df

