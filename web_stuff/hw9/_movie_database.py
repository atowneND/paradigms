# Ashley Towne
# 2/24/2016
# python primer

import csv

class _movie_database:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.ratings = {}
    
    def load_one_movie(self, movie_file, mid):
        with open(movie_file) as f:
            for line in f:
                line = line.rstrip()
                movie_attr = line.split("::")
                if (int(movie_attr[0])==int(mid)):
                    self.movies[int(movie_attr[0])] = {'title':movie_attr[1],'genres':movie_attr[2]}
                    break

    def load_movies(self, movie_file):
        self.movies = {}
        with open(movie_file) as f:
            for line in f:
                line = line.rstrip()
                movie_attr = line.split("::") # movie attributes
                self.movies[int(movie_attr[0])] = {'title':movie_attr[1],'genres':movie_attr[2]}

    def get_movie(self, mid):
        if mid not in self.movies:
            return None
        else:
            return [self.movies[mid]['title'], self.movies[mid]['genres']]

    def get_movies(self):
        return [i for i in self.movies]

    def set_movie(self, mid, movie):
        self.movies[mid] = {'title':movie[0],'genres':movie[1]}

    def delete_movie(self, mid):
        self.movies.pop(mid,None)

    def load_users(self, users_file):
        self.users = {}
        with open(users_file) as f:
            for line in f:
                line = line.rstrip()
                user_attr = line.split("::") # user attributes
                self.users[int(user_attr[0])] = {'gender':user_attr[1], 'age':user_attr[2], 'occupation':user_attr[3], 'zipcode':user_attr[4]}

    def get_user(self, uid):
        if uid not in self.users:
            return None
        else:
            return [self.users[uid]['gender'], int(self.users[uid]['age']), int(self.users[uid]['occupation']), self.users[uid]['zipcode']]
    
    def get_users(self):
        return [i for i in self.users]

    def set_user(self, uid, user_attr):
        self.users[uid] = {'gender':user_attr[0], 'age':user_attr[1], 'occupation':user_attr[2], 'zipcode':user_attr[3]}

    def delete_user(self, uid):
        self.users.pop(uid,None)

    def load_ratings(self, ratings_file):
        self.ratings = {}
        with open (ratings_file) as f:
            for line in f:
                line = line.rstrip()
                rate_attr = line.split("::") # rating attributes
                mid = int(rate_attr[1])
                uid = int(rate_attr[0])
                if mid not in self.ratings:
                    self.ratings[mid] = {uid:int(rate_attr[2])}
                else:
                    self.ratings[mid][uid] = float(rate_attr[2])

    def get_rating(self, mid):
        if mid not in self.ratings:
            return None
        else: 
            vals = self.ratings[mid].values()
            return float( sum(vals))/float(len(vals))

    def get_highest_rated_movie(self):
        return max(
                sorted([[mid, self.get_rating(mid)] for mid in self.ratings],
                        key = lambda x: x[0],
                    ),
                key = lambda x:(x[1], -x[0]),
            )[0]

    def get_recommended_movie(self, uid):
        return max(
                sorted(
                        [
                            [mid, self.get_rating(mid)] if self.get_user_movie_rating(uid, mid) is None else [0,0] 
                            for mid in self.ratings
                            ],
                        key = lambda x: x[0],
                    ),
                key = lambda x:(x[1], -x[0]),
            )[0]

    def set_user_movie_rating(self, uid, mid, rating):
        self.ratings[mid][uid] = float(rating)

    def get_user_movie_rating(self, uid, mid):
        if (mid not in self.ratings) or (uid not in self.ratings[mid]):
            return None
        return self.ratings[mid][uid]

    def delete_all_ratings(self):
        self.ratings.clear()

if __name__ == '__main__':
    m = _movie_database()
    m.load_movies('ml-1m/movies.dat')
    print m.get_movie(119)
