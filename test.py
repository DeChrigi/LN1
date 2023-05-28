import db_access
import pandas as pd 

df = db_access.get_top_songs()
df_bar = df.assign(Genres=df['Genres'].str.split(', ')).explode('Genres')

df_group_by = df_bar.groupby(['Genres']).agg({'Tempo': 'mean'})
print(type(df_group_by))

