import pandas as pd
import re

def extract():
    df=pd.read_csv('featuresdf.csv',sep=',')
    return df

def transform(df):
    
    variable = True

    df.drop(columns=['id','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature'], inplace = True)
    entrada = input('¿Qué artista te gustaría escuchar?:\n').strip()
    canciones = []
    for i in range(len(df)):
        if re.fullmatch(entrada, df['artists'][i], flags=re.I) != None:
            canciones.append(df['name'][i])

    if len(canciones) == 0:
        no_rec = 'El recomendador no reconoce al artista'
        return no_rec
    else:
        data = {'canciones': canciones, 'artista': [entrada for _ in range(len(canciones))]}
        df_artista = pd.DataFrame(data)
        return df_artista
            
def load(data):
    print(data)

if __name__ == '__main__':
    df = extract()
    data = transform(df)
    load(data)