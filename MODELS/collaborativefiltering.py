import pandas as pd
import numpy as np
import os

class CollaborativeRecommender :
    
    def __init__(self, ratings: pd.DataFrame, userid, titleid, ratingid, highestRating : int, thresh = 10) -> None:
        self.putDataset(ratings, userid, titleid, ratingid, highestRating )
        self.correlationMatrix = pd.DataFrame()
        self.thresh = thresh
        self.ratingsByUserId = pd.DataFrame()
        
    def saveCorrelationMatrix(self, filename:str):
        self.correlationMatrix.to_pickle(filename)
        
    def loadCorrelationMatrix(self, filename:str):
        if(os.path.isfile(filename)):
            self.correlationMatrix = pd.read_pickle(filename)
        else:
            pass
        
    def putDataset(self, ratings: pd.DataFrame, userid: str, titleid: str, ratingid: str, highestRating : int)-> None:
        self.ratings = ratings
        self.userid = userid
        self.titleid = titleid
        self.ratingid = ratingid
        self.highestRating = highestRating
        
    def putPrefs(self, listOfMovieRatings):
        self.prefs = listOfMovieRatings
        
    def getRatingsByUserId(self) -> pd.DataFrame:
        if self.ratingsByUserId.empty:
            self.gratings = self.ratings.groupby(self.titleid).filter(lambda x: len(x) >= self.thresh).groupby(self.userid).filter(lambda x: len(x)>=self.thresh)
            self.ratingsByUserId =  self.gratings.pivot_table(index=self.userid,columns=self.titleid,values=self.ratingid)
        return self.ratingsByUserId
    
    
    def getCorrelationMatrix(self,ratingByUserId :pd.DataFrame) -> pd.DataFrame:
        corrmatrix = np.corrcoef(ratingByUserId.fillna(0, axis=1).values, rowvar=False)
        ax = self.getSearchableList()
        self.correlationMatrix =  pd.DataFrame(corrmatrix, index =ax, columns=ax )
        # self.correlationMatrix = ratingByUserId.fillna(0, axis= 1).corr(method='pearson')
        return self.correlationMatrix
    
    def getSearchableList(self) :
        return self.getRatingsByUserId().columns.tolist()
        
    
    def getSimilarToMovie(self, movie_name,rating):
        if self.correlationMatrix.empty:
            similar_ratings = self.getCorrelationMatrix(
                self.getRatingsByUserId(),
                )[movie_name]*(rating-float(self.highestRating)/2)
        else:
            similar_ratings = self.correlationMatrix[movie_name]*(rating-float(self.highestRating)/2)
        similar_ratings = similar_ratings.sort_values(ascending=False)
        return similar_ratings
    
    def getSimilarToMovies(self, num):
        similar_movies = pd.DataFrame()
        similar_movies = pd.concat([self.getSimilarToMovie(movie, rating) for movie, rating in self.prefs],  axis=1,ignore_index=True)
        similar_movies = similar_movies.sum('columns').sort_values(ascending=False).head(num)
        return similar_movies
    
    def find_closest_matches(self, query):
        matches = []
        objects = self.getSearchableList()
        for moviez in objects:
            # print(query.lower(), moviez.lower())
            if query.lower() in moviez.lower() :
                matches.append(moviez)

        return matches       
   

def preprocessMovies():
    ratings = pd.read_csv('./CSV/movies-dataset/movie_ratings.csv')
    movies = pd.read_csv('./CSV/movies-dataset/movies.csv')
    ratings = pd.merge(movies,ratings) .drop(['genres','timestamp'],axis=1)
    return ratings

def preprocessBooks():
    ratings = pd.read_csv('./CSV/books-dataset/Ratings.csv')
    books = pd.read_csv('./CSV/books-dataset/Books.csv', low_memory= False)
    bookratin = pd.merge(books, ratings)[['ISBN', 'Book-Title', 'User-ID', 'Book-Rating']]
    # print(bookratin[bookratin.duplicated(['ISBN', 'User-ID'])])
    return bookratin
