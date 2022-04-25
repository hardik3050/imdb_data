import pandas as pd
from sqlalchemy import create_engine

imdb = pd.read_csv ('/Users/hardikrathod/Desktop/Final_project/big-bang-theory-dataset-assessment/data/imdb.csv')
df_imdb = pd.DataFrame(imdb, columns= ['season','episode_num','title','original_air_date','imdb_rating','total_votes','desc'])

engine = create_engine('sqlite:///imdb.db', echo=True)
sqlite_connection = engine.connect()
df_imdb.to_sql('tbimdb', sqlite_connection, index=False)


episodes = pd.read_csv ('/Users/hardikrathod/Desktop/Final_project/big-bang-theory-dataset-assessment/data/episodes.csv')
df_episodes = pd.DataFrame(episodes, columns= ['season','episode_num_in_season', 'episode_num_overall',	'title', 'directed_by',	'written_by', 'original_air_date', 'prod_code', 'us_viewers'])
df_episodes[['Story by:','Teleplay by:']] = pd.DataFrame(df_episodes['written_by'].str.strip("Story by: ").str.split("Teleplay by: ", expand=True))
df_episodes.to_sql('tbepisodes', sqlite_connection, index=False)




