import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender :
    def putDataset(self, ratings: pd.DataFrame, userid, titleid, ratingid, highestRating : int):
        self.ratings = ratings
        self.userid = userid
        self.titleid = titleid
        self.ratingid = ratingid
        self.highestRating = highestRating
    def putPrefs(self, listOfMovieRatings):
        self.moviePrefs = listOfMovieRatings
        
    def getRatingsByUserId(self):
        # debugging
        self.ratings = self.ratings.groupby(self.userid).filter(lambda x: len(x) >= 200)
        print(self.ratings)
        self.ratingsByUserId =  self.ratings.pivot_table(index=self.userid,columns=self.titleid,values=self.ratingid).dropna(thresh=10, axis='columns').fillna(0,axis=1)
        return self.ratingsByUserId
    
    def getCorrelationMatrix(ratingByUserId : pd.DataFrame):
        return ratingByUserId.corr(method='pearson')
    
    def getSimilarToMovie(self, movie_name,rating):
        similar_ratings = MovieRecommender.getCorrelationMatrix(self.getRatingsByUserId())[movie_name]*(rating-float(self.highestRating)/2)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings
    
    def getSimilarToMovies(self):
        similar_movies = pd.DataFrame()
        similar_movies = pd.concat([self.getSimilarToMovie(movie, rating) for movie, rating in self.moviePrefs],  axis=1,ignore_index=True)
        similar_movies = similar_movies.sum('columns').sort_values(ascending=False).head(20)
        return similar_movies

def preprocessMovies():
    ratings = pd.read_csv('dataset/ratings.csv')
    movies = pd.read_csv('dataset/movies.csv')
    ratings = pd.merge(movies,ratings) .drop(['genres','timestamp'],axis=1)
    return ratings

def preprocessBooks():
    ratings = pd.read_csv('books-dataset/Ratings.csv')
    books = pd.read_csv('books-dataset/Books.csv', low_memory= False)
    bookratin = pd.merge(books, ratings)[['ISBN', 'Book-Title', 'User-ID', 'Book-Rating']]
    print(bookratin[bookratin.duplicated(['ISBN', 'User-ID'])])
    return bookratin
def test():
    movieratings = preprocessMovies()
    bookratings = preprocessBooks()
    print(bookratings.head(20))
    print(movieratings.head(20))
    recommender = MovieRecommender()
    bookrecom = MovieRecommender()
    bookrecom.putDataset(bookratings, 'User-ID', 'Book-Title', 'Book-Rating', 10)
    recommender.putDataset(movieratings, 'userId', 'title', 'rating', 5)
    newprefs = [(2,4), (3,5), (34, 2)]
    testprefs = [("Shawshank Redemption, The (1994)",5),("Alice in Wonderland (2010)",1),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
    bookprefs = [["It", 8]]
    bookrecom.putPrefs(bookprefs)
    recommender.putPrefs(testprefs)
   
    print(recommender.getSimilarToMovies())
    print(bookrecom.getSimilarToMovies())
    
test()