# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def good_movie(movie):
    if movie["imdb"]>5.5:
        return True
    return False
def good_movie_list(movies):
    listOfGoodMovies=[]
    for i in movies:    
        if i["imdb"]>5.5:
            listOfGoodMovies.append(i)
    return listOfGoodMovies
def category(movies):
    ctg=input('category: ')
    listCategory=[]
    for i in movies:    
        if i["category"]==ctg:
            listCategory.append(i)
    return listCategory
def avg_imdb(movies):
    avgIMDB=0
    for i in movies: 
        avgIMDB=avgIMDB+i["imdb"]
    return avgIMDB/len(movies)
def avg_imdb_by_category(movies):
    sum1=0
    cnt=0
    ctg=input('category: ')
    for i in movies: 
        if i["category"]==ctg:
            sum1=sum1+i["imdb"]
            cnt=cnt+1
    return sum1/cnt


print(good_movie(movies[0]))
print(good_movie_list(movies))
print(category(movies))
print(avg_imdb(movies))
print(avg_imdb_by_category(movies))
