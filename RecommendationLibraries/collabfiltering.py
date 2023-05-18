import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender :
    def putDataset(self, ratings: pd.DataFrame):
        self.ratings = ratings
        
    def putMoviePrefs(self, listOfMovieRatings):
        self.moviePrefs = listOfMovieRatings
        
    def getRatingsByUserId(self):
        self.ratingsByUserId =  self.ratings.pivot_table(index=['userId'],columns=['title'],values='rating').dropna(thresh=10, axis='columns').fillna(0,axis=1)
        return self.ratingsByUserId
    
    def getCorrelationMatrix(ratingByUserId : pd.DataFrame):
        return ratingByUserId.corr(method='pearson')
    
    def getSimilarToMovie(self, movie_name,rating):
        similar_ratings = MovieRecommender.getCorrelationMatrix(self.getRatingsByUserId())[movie_name]*(rating-2.5)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings
    
    def getSimilarToMovies(self):
        similar_movies = pd.DataFrame()
        similar_movies = pd.concat([self.getSimilarToMovie(movie, rating) for movie, rating in self.moviePrefs],  axis=1,ignore_index=True)
        similar_movies = similar_movies.sum('columns').sort_values(ascending=False).head(20)
        return similar_movies

def preprocess():
    ratings = pd.read_csv('dataset/ratings.csv')
    movies = pd.read_csv('dataset/movies.csv')
    ratings = pd.merge(movies,ratings) .drop(['genres','timestamp'],axis=1)
    return ratings

def test():
    ratings = preprocess()
    recommender = MovieRecommender()
    recommender.putDataset(ratings)
    print(recommender.ratings.head())
    testprefs = [("Avengers, The (2012)",5),("Alice in Wonderland (2010)",1),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
    recommender.putMoviePrefs(testprefs)
    print(recommender.getSimilarToMovies())
    
test()