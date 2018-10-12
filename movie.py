#IMDB
import csv
import numpy as np
reader = csv.reader(open("movie_metadata.csv", "rb"), delimiter=",")
x = list(reader)
result = np.array(x).astype("string")
listl = []
listm = []
listn = []
score = []
listmovie = []
databasemovie = []
databasemovietitle = []
for i in range(1,10):
    listmovie = []
    l = result[i, 25]
    listmovie.append(l)
    m = result[i, 27]
    listmovie.append(m)
    n = result[i, 8]
    listmovie.append(n)
    fltl = float(str(l))
    fltm = float(str(m))
    t = result[i, 11]
    databasemovietitle.append(t)
    if fltm == 0:
        fltm = fltl*10000 + fltn/10000.0
        print t,"-->",fltm
    try:
        fltn = float(str(n))
    except:
        fltn = fltm*1000.0 + fltl*1000000.0
        print t,"-->",fltn
    # try:
    #     fltm = float(str(m))
    #     fltn = float(str(n))
    # except:
    #     try:
    #         fltm = 0
    #         fltn = float(str(n))
    #     except:
    #         try:
    #             fltm = float(str(m))
    #             fltn = 0
    #         except:
    #             fltm = 0
    #             fltn = 0
    k = fltl*10000.0 + fltm + fltn/100000.0
    score.append(k)
    databasemovie.append(listmovie)
data = np.array([databasemovie])
target = []
# print data
# print score
avg = sum(score)/len(score)
print avg

for i in range(1, len(databasemovietitle)):
    if score[i] > avg:
        target.append(1)
        print 1,"          ",databasemovietitle[i],"-->",databasemovie[i],"-->",score[i]
    else:
        target.append(0)
        print 0,"          ",databasemovietitle[i],"-->",databasemovie[i],"-->",score[i]
print target
