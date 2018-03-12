import pandas as pd 

df=pd.read_csv("IMDB_data.csv",encoding="ISO-8859-1",skiprows=[2],header=[0])
a=df['Genre'].value_counts()
b=a.keys()
c=[]
for i in b:
	c=c+[a[i]]

df1=pd.DataFrame({'Genre':b,'Freq':c})

for i in range(0,len(df['imdbVotes'])):
	try:
		df['imdbVotes'][i]=int(df['imdbVotes'][i])
	except AttributeError:
		df['imdbVotes'][i]=0
	except ValueError:
		df['imdbVotes'][i]=0	

for i in range(0,len(df['imdbRating'])):
	try:
		df['imdbRating'][i]=int(df['imdbRating'][i])
	except AttributeError:
		df['imdbRating'][i]=0
	except ValueError:
		df['imdbRating'][i]=0	

for i in range(0,len(df['Year'])):
	try:
		df['Year'][i]=int(df['Year'][i])
	except AttributeError:
		df['Year'][i]=0
	except ValueError:
		df['Year'][i]=0

print(df.sort_values(['Genre'], ascending=[True]))
df['newVar']=(df['imdbRating']-df['imdbVotes'])*(df['imdbRating']-df['imdbVotes'])
print(df['newVar'])
