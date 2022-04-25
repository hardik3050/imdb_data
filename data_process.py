from cgi import test
import pandas as pd

episodes = pd.read_csv ('/Users/hardikrathod/Desktop/Final_project/big-bang-theory-dataset-assessment/data/episodes.csv')
imdb = pd.read_csv ('/Users/hardikrathod/Desktop/Final_project/big-bang-theory-dataset-assessment/data/imdb.csv')

df_episodes = pd.DataFrame(episodes, columns= ['season','episode_num_in_season', 'episode_num_overall',	'title', 'directed_by',	'written_by', 'original_air_date', 'prod_code', 'us_viewers'])
df_imdb = pd.DataFrame(imdb, columns= ['season','episode_num','title','original_air_date','imdb_rating','total_votes','desc'])


df_episodes[['Story by:','Teleplay by:']] = pd.DataFrame(df_episodes['written_by'].str.strip("Story by: ").str.split("Teleplay by: ", expand=True))
df_episodes.to_csv('./test.csv', encoding='utf-8', index=False)
print(df_episodes)




