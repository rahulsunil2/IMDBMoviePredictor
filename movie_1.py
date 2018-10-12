# Import
import csv
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#Fta

#GenFromTXT
train = pd.read_csv("movie_metadata.csv")
train["num_critic_for_reviews"] = train["num_critic_for_reviews"].fillna(train.num_critic_for_reviews.median())
train["gross"] = train["gross"].fillna(train.gross.median())
train["imdb_score"] = train["imdb_score"].fillna(train.imdb_score.median())
train["movie_facebook_likes"] = train["movie_facebook_likes"].fillna(train.movie_facebook_likes.median())
# reader = list(csv.reader(open("movie_metadata.csv", "rb"), delimiter=","))
movie = np.array(train)
header = movie[0,:]
movie = movie[1:,:]
imdb_score = movie[:,25]
fb_likes = movie[:,27]
gross = movie[:,8]
movie_name = movie[:,11]
num_critics = movie[:,2]
data = np.column_stack((imdb_score ,fb_likes, gross, num_critics))
data.astype(float)

#KMeans

model = KMeans(n_clusters=2)
model.fit(data)
KMeans(algorithm="auto")
labels = model.predict(data)

print labels

#Predictions Printing

movie_title = np.array(train["movie_title"]).astype(str)
my_solution = pd.DataFrame(labels, movie_name, columns = ["Watch[1] or Not[0]"])

#Save to CSV

my_solution.to_csv("my_solution_one.csv", index_label = ["movie_title"])

#Plot

xs = data[:,0]
ys = data[:,2]
plt.scatter(xs, ys, c=labels)
plt.show()
