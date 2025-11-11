import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\gowth\OneDrive\Desktop\movies rating.csv")
print(df)

# delet command:
del df['ReleaseYear']
print(df)


print(df.shape)
print("Average Rating:", df["Rating"].mean())
print("Total Movies:", df["Title"].unique())
print("Languages:", df["Language"].unique())
print("streaming_plotform:", df["Streaming_Platform"].unique())

# null values:
print("Null values per columns:")
print(df.isnull().sum())


# A movie streaming platform wants to analyze movie ratings:
rating=df[(df['Rating']>="4.5")]
print(rating)

# Top rated movies:
amazon_prime = df[(df['Streaming_Platform'] == "Amazon Prime") & (df['Rating'] >="4.0")]
print("Good Movies",amazon_prime)
hotstar= df[(df['Streaming_Platform'] == "Hotstar") & (df['Rating'] >="4.0")]
print("Good Movies",hotstar)
netflix= df[(df['Streaming_Platform'] == "Netflix") & (df['Rating'] >="4.0")]
print("Good Movies",netflix)

# Average rated movies:
amazon_prime = df[(df['Streaming_Platform'] == "Amazon Prime") & (df['Rating'] >="2.6") & (df['Rating']<="3.9")]
print("Average Movies",amazon_prime)
hotstar= df[(df['Streaming_Platform'] == "Hotstar") & (df['Rating'] >="2.6") & (df['Rating']<="3.9")]
print("Average Movies",hotstar)
netflix= df[(df['Streaming_Platform'] == "Netflix") & (df['Rating'] >="2.6") & (df['Rating']<="3.9")]
print("Average Movies",netflix)

# below Average or Worst rated movies:
amazon_prime = df[(df['Streaming_Platform'] == "Amazon Prime") & (df['Rating'] >="0.1") & (df['Rating']<="2.5")]
print("Below Average Movies",amazon_prime)
hotstar= df[(df['Streaming_Platform'] == "Hotstar") & (df['Rating'] >="0.1") & (df['Rating']<="2.5")]
print("Below Average Movies",hotstar)
netflix= df[(df['Streaming_Platform'] == "Netflix") & (df['Rating'] >="0.1") & (df['Rating']<="2.5")]
print("Below Average Movies",netflix)



# Data modeling and EDA(PYTHON):
# Ratings like datasets to find Gerne and Actor:

dataset = df[(df['Actor'] == "Suriya") & (df['Genre'] =="Romance") & (df['Rating']>="4.0")]
print(dataset)

dataset = df[(df['Actor'] == "Dulquer Salmaan") & (df['Genre'] =="Mystery") & (df['Rating']>="4.1")]
print(dataset)

dataset = df[(df['Actor'] == "Vijay") & (df['Genre'] =="Thriller") & (df['Rating']>="3.9")]
print(dataset)


# Graph for Movie Rating:

# scatter chart
# plt.figure(figsize=(16,6))
# sns.scatterplot(x='Language', y='Streaming_Platform', data=df, s=100, palette='cool')
# plt.title("LANGUAGE AND STREAMING PLATFORM")
# plt.show()

# line chart
# plt.figure(figsize=(18,8))
# sns.lineplot(x='Actor', y='Title', data=df, marker='o', color='olive')
# plt.title("ACTORS AND MOVIE TITLES")
# plt.show()

# bar chart
# plt.figure(figsize=(18,7))
# sns.barplot(x='Language', y='ReleaseYear', data=df, palette='YlGn')
# plt.title("LANGUAGE AND REALESE_YEAR")
# plt.show()


from sqlalchemy import create_engine
username="root"
password="root"
host="localhost"
port="3306"
database="fitaproject"

engine=create_engine(f"mysql+pymysql://root:root@localhost:3306/fitaproject")
table_name="students"
df.to_sql(table_name,engine,if_exists='replace',index=False)
